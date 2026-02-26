# Quick Reference Guide

## CSS Files Quick Lookup

| File | Purpose | Used By |
|------|---------|---------|
| base.css | Global styles, variables, typography | All pages |
| navbar.css | Navigation bar styling | All pages |
| hero.css | Hero section backgrounds | home, all pages |
| cards.css | Card components | home, all pages |
| forms.css | Forms and input styling | predict, analyze |
| predict.css | Predict page specific | predict.html |
| analyze.css | Analyze page specific | analyze.html |
| weather.css | Weather page specific | weather.html |
| market.css | Market table styling | market.html |
| schemes.css | Schemes cards styling | schemes.html |

## JavaScript Files Quick Lookup

| File | Key Functions | Used By |
|------|---------------|---------|
| utility.js | Storage, Dom, Math, Arrays, Strings, Dates | All pages |
| main.js | Notifications, validation, API calls | All pages |
| predict.js | Form handling, results display | predict.html |
| analyze.js | Image upload, preview, analysis | analyze.html |

## Common Tasks & Solutions

### Display a Notification
```javascript
showNotification('Success!', 'success');
showNotification('Error!', 'error');
showNotification('Warning!', 'warning');
```

### Make an API Call
```javascript
const result = await apiCall('/api/predict', 'POST', {
    crop: 'rice',
    temperature: 25,
    humidity: 60
});
```

### Validate a Form
```javascript
if (validateForm('myForm')) {
    // Form is valid
}
```

### Store Data Locally
```javascript
Storage.set('userPreference', { theme: 'dark' });
const preference = Storage.get('userPreference');
Storage.remove('userPreference');
```

### DOM Manipulation
```javascript
const element = Dom.getElementById('myId');
Dom.addClass(element, 'active');
Dom.show(element);
```

### Format Dates
```javascript
const formatted = DateUtils.format(new Date(), 'YYYY-MM-DD');
const nextWeek = DateUtils.addDays(new Date(), 7);
```

## CSS Classes Reference

### Navbar Classes
```css
.navbar              /* Main navbar container */
.navbar .logo       /* Logo styling */
.navbar a           /* Navigation links */
.navbar a.active    /* Active page link */
```

### Form Classes
```css
.form-container     /* Form wrapper */
.form-group         /* Form field group */
input, textarea     /* Input elements */
button[type="submit"] /* Submit buttons */
.btn-secondary      /* Secondary button */
.btn-danger         /* Danger button */
#result.success     /* Success message */
#result.error       /* Error message */
```

### Card Classes
```css
.cards              /* Card container */
.card               /* Individual card */
.icon               /* Card icons */
.info-section       /* Info cards section */
.info-card          /* Individual info card */
```

### Page-Specific Classes
```css
/* Predict */
.prediction-result
.prediction-details
.detail-item

/* Analyze */
.image-preview
.disease-result
.recommendations

/* Weather */
.weather-card
.weather-details
.alert-box

/* Market */
.market-table
.market-container

/* Schemes */
.scheme-item
.scheme-button
.scheme-description
```

## Color Palette

```css
Primary Green:   #4CAF50  (Success, primary actions)
Secondary Blue:  #2196F3  (Secondary actions, info)
Warning Orange:  #FF9800  (Warnings, alerts)
Danger Red:      #f44336  (Errors, danger)
Dark Gray:       #333     (Text, headings)
Light Gray:      #f9f9f9  (Backgrounds)
White:           #ffffff  (Cards, containers)
```

## Responsive Breakpoints

```css
Desktop:  > 768px
Tablet:   481px - 768px
Mobile:   < 480px
```

## File Import Checklist

When creating a new page template:
- [ ] Include base.css
- [ ] Include navbar.css
- [ ] Include hero.css
- [ ] Include cards.css
- [ ] Include forms.css (if form-heavy)
- [ ] Include page-specific CSS
- [ ] Include utility.js
- [ ] Include main.js
- [ ] Include page-specific JS
- [ ] Add meta viewport tag
- [ ] Add appropriate title

## Common Patterns

### Success Pattern
```html
<div id="result" class="prediction-result">
    <!-- Success content -->
</div>
```

```javascript
showNotification('Success!', 'success');
```

### Error Handling Pattern
```javascript
try {
    const result = await apiCall(url, 'POST', data);
    showNotification('Done!', 'success');
} catch (error) {
    showNotification('Error: ' + error, 'error');
}
```

### Form Submission Pattern
```javascript
document.getElementById('myForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    if (!validateForm('myForm')) {
        showNotification('Please fill all fields', 'warning');
        return;
    }
    
    showLoader();
    // Make API call
    hideLoader();
});
```

## Performance Tips

1. **Use Storage API** for client-side caching
2. **Debounce** input handlers with throttle()
3. **Lazy load** images where possible
4. **Minimize inline styles** - use CSS classes
5. **Use apiCall()** for consistent error handling
6. **Cache API responses** in Storage

## Browser Support

- Chrome/Edge: Full support
- Firefox: Full support
- Safari: Full support (11+)
- Mobile browsers: Full support

## Accessibility Considerations

1. Use semantic HTML (form, button, etc.)
2. Include proper labels for inputs
3. Use ARIA attributes where needed
4. Maintain color contrast ratio of 4.5:1
5. Keyboard navigation support through navbar

## Testing Checklist

When modifying files:
- [ ] Test on desktop browser
- [ ] Test on mobile browser
- [ ] Test form submissions
- [ ] Test API calls
- [ ] Test notifications
- [ ] Check console for errors
- [ ] Verify styles applied correctly

---
Last Updated: February 2026
Version: 1.0




## pipeline of cropyield

1. Data Ingestion
   → Read from MongoDB
   → Save raw data

2. Data Validation
   → Check schema
   → Check nulls

3. Data Transformation  ✅ (YOUR OUTLIERS HERE)
   → Remove outliers
   → Log transform
   → Scaling

4. Model Training
