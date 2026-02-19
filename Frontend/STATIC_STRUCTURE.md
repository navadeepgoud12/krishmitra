# KrishMitra - Static Files Organization

## Overview
Your static files are now organized into separate, modular CSS and JavaScript files for better maintainability and reusability.

## Directory Structure

```
Frontend/
├── static/
│   ├── CSS Files
│   │   ├── base.css           (Global styles & variables)
│   │   ├── navbar.css         (Navigation styling)
│   │   ├── hero.css           (Hero section)
│   │   ├── cards.css          (Card components)
│   │   ├── forms.css          (Forms & buttons)
│   │   ├── predict.css        (Predict page)
│   │   ├── analyze.css        (Analyze page)
│   │   ├── weather.css        (Weather page)
│   │   ├── market.css         (Market page)
│   │   └── schemes.css        (Schemes page)
│   │
│   ├── JavaScript Files
│   │   ├── main.js            (Common utilities)
│   │   ├── utility.js         (Helper functions)
│   │   ├── predict.js         (Predict page logic)
│   │   └── analyze.js         (Analyze page logic)
│   │
│   └── home.css              (Old - can be deleted)
│
└── templates/
    ├── home.html
    ├── predict.html
    ├── analyze.html
    ├── weather.html
    ├── market.html
    └── schemes.html
```

## CSS Files Description

### Base & Common
**base.css**
- Global styles and resets
- Color variables (--primary-color, --secondary-color, etc.)
- Typography defaults
- Link styling

**navbar.css**
- `.navbar` - Main navbar container
- `.navbar ul` - Navigation list
- `.navbar a` - Navigation links with hover effects
- `.navbar a.active` - Active page indicator

**hero.css**
- `.hero` - Hero section container
- `.content` - Content wrapper
- `.overlay` - Background overlay
- Responsive design for mobile

**cards.css**
- `.cards` - Card container
- `.card` - Individual card styling
- `.icon` - Card icons
- `.info-section` - Info cards section
- `.info-card` - Info card styling
- Hover effects and transitions

**forms.css**
- Form element styling (input, textarea, select)
- Button styling (.btn-primary, .btn-secondary, .btn-danger)
- Form validation styles
- `.form-container` - Form wrapper
- `.form-group` - Form field grouping
- Error and success states

### Page-Specific CSS
**predict.css** - Prediction form and results styling
**analyze.css** - Disease analysis and image preview styling
**weather.css** - Weather cards and forecast layout
**market.css** - Market table and price display styling
**schemes.css** - Government schemes listing and details

## JavaScript Files Description

### main.js
Essential utility functions for all pages:

```javascript
// Notifications
showNotification(message, type, duration)  // type: 'success', 'error', 'warning', 'info'

// Validation
isValidEmail(email)
validateForm(formId)

// API
apiCall(url, method, data)  // method: 'GET', 'POST', etc.

// Loader
showLoader()
hideLoader()

// Formatting
capitalizeFirstLetter(string)
formatDate(date)
formatNumber(number)

// Debouncing
debounce(func, delay)
```

### utility.js
Advanced utility objects and functions:

```javascript
// Local Storage
Storage.set(key, value)
Storage.get(key)
Storage.remove(key)
Storage.clear()

// Cookies
Cookie.set(name, value, days)
Cookie.get(name)
Cookie.remove(name)

// DOM Manipulation
Dom.getElementById(id)
Dom.querySelector(selector)
Dom.hasClass(element, className)
Dom.addClass(element, className)
Dom.removeClass(element, className)
Dom.show(element)
Dom.hide(element)

// Math Utilities
Math2.roundTo(num, decimals)
Math2.percentage(part, whole)
Math2.random(min, max)

// Array Utilities
ArrayUtils.shuffle(array)
ArrayUtils.unique(array)
ArrayUtils.groupBy(array, key)

// String Utilities
StringUtils.capitalize(str)
StringUtils.truncate(str, length)
StringUtils.replaceAll(str, search, replace)

// Date Utilities
DateUtils.now()
DateUtils.format(date, format)
DateUtils.addDays(date, days)

// Advanced Functions
throttle(func, limit)  // Limit function call frequency
isInViewport(element)  // Check if element is visible
```

### predict.js
Prediction page functionality:

```javascript
handlePredictSubmit(e)          // Form submission handler
displayPredictionResult(...)    // Display prediction results
resetPredictForm()              // Clear form
exportPrediction()              // Export as CSV
```

### analyze.js
Disease analysis functionality:

```javascript
handleAnalyzeSubmit(e)          // Form submission handler
previewImage(e)                 // Preview selected image
displayAnalysisResult(...)      // Display analysis results
resetAnalyzeForm()              // Clear form
downloadReport()                // Download analysis report
```

## CSS Variables (from base.css)

```css
--primary-color: #4CAF50      /* Green */
--secondary-color: #2196F3    /* Blue */
--warning-color: #FF9800      /* Orange */
--danger-color: #f44336       /* Red */
--success-color: #4CAF50      /* Green */
--dark: #333                  /* Dark gray */
--light: #f9f9f9              /* Light gray */
```

## How to Include Files in HTML

### All pages should include:
```html
<link rel="stylesheet" href="{{ url_for('static', filename='base.css') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='navbar.css') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='hero.css') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='cards.css') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='forms.css') }}">

<script src="{{ url_for('static', filename='utility.js') }}"></script>
<script src="{{ url_for('static', filename='main.js') }}"></script>
```

### Page-specific additions:
```html
<!-- For Predict page -->
<link rel="stylesheet" href="{{ url_for('static', filename='predict.css') }}">
<script src="{{ url_for('static', filename='predict.js') }}"></script>

<!-- For Analyze page -->
<link rel="stylesheet" href="{{ url_for('static', filename='analyze.css') }}">
<script src="{{ url_for('static', filename='analyze.js') }}"></script>

<!-- For Weather page -->
<link rel="stylesheet" href="{{ url_for('static', filename='weather.css') }}">

<!-- For Market page -->
<link rel="stylesheet" href="{{ url_for('static', filename='market.css') }}">

<!-- For Schemes page -->
<link rel="stylesheet" href="{{ url_for('static', filename='schemes.css') }}">
```

## Common Styling Patterns

### Form Container
```html
<div class="form-container">
    <h3>Form Title</h3>
    <form id="myForm">
        <input type="text" placeholder="Name" required>
        <button type="submit">Submit</button>
    </form>
    <div id="result"></div>
</div>
```

### Info Card
```html
<div class="info-card">
    <h3>Title</h3>
    <p>Content</p>
    <button>Action</button>
</div>
```

### Notification
```javascript
// Success notification
showNotification('Action completed!', 'success');

// Error notification
showNotification('Error occurred!', 'error');

// Warning notification
showNotification('Please be careful!', 'warning');
```

## Responsive Design
All CSS files include mobile-first responsive design with breakpoints at:
- Tablet: 768px
- Mobile: 480px

## Next Steps
1. You can now safely delete the old `home.css` file
2. All new pages should follow the current structure
3. To add new features, create page-specific CSS and JS files
4. Keep common styles in `base.css`
5. Use the utility functions for consistency

## File Sizes (Approximate)
- base.css: 1.2 KB
- navbar.css: 1.0 KB
- hero.css: 0.8 KB
- cards.css: 2.5 KB
- forms.css: 3.0 KB
- Page-specific CSS: 1-2 KB each
- main.js: 4.5 KB
- utility.js: 5.5 KB
- Page-specific JS: 3-4 KB each

Total organized structure is modular and maintainable!
