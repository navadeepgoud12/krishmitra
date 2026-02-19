# Static Assets Structure

## CSS Files (in Frontend/static/)

### Base & Common
- **base.css** - Global styles, variables, and typography
- **navbar.css** - Navbar styling and navigation
- **hero.css** - Hero section styling
- **cards.css** - Card and info-card components
- **forms.css** - Form elements and buttons styling

### Page-Specific CSS
- **predict.css** - Predict page styling
- **analyze.css** - Analyze page styling
- **weather.css** - Weather page styling
- **market.css** - Market prices page styling
- **schemes.css** - Government schemes page styling

## JavaScript Files (in Frontend/static/)

### Base & Common
- **main.js** - Common functions (notifications, validation, API calls)
- **utility.js** - Utility functions (Storage, Dom, Math, Arrays, Strings, etc.)

### Page-Specific JS
- **predict.js** - Predict page functionality
- **analyze.js** - Analyze page functionality

## How to Include in HTML

```html
<!-- CSS Files -->
<link rel="stylesheet" href="{{ url_for('static', filename='base.css') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='navbar.css') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='hero.css') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='cards.css') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='forms.css') }}">

<!-- Page-specific CSS -->
<link rel="stylesheet" href="{{ url_for('static', filename='[page].css') }}">

<!-- JS Files -->
<script src="{{ url_for('static', filename='utility.js') }}"></script>
<script src="{{ url_for('static', filename='main.js') }}"></script>

<!-- Page-specific JS -->
<script src="{{ url_for('static', filename='[page].js') }}"></script>
```

## Usage Examples

### In predict.html
```html
<link rel="stylesheet" href="{{ url_for('static', filename='predict.css') }}">
<script src="{{ url_for('static', filename='predict.js') }}"></script>
```

### In analyze.html
```html
<link rel="stylesheet" href="{{ url_for('static', filename='analyze.css') }}">
<script src="{{ url_for('static', filename='analyze.js') }}"></script>
```

## Functions Available

### From main.js
- `showNotification(message, type, duration)` - Show toast notifications
- `isValidEmail(email)` - Validate email
- `validateForm(formId)` - Validate form fields
- `apiCall(url, method, data)` - Make API calls
- `showLoader()` - Show loading spinner
- `hideLoader()` - Hide loading spinner

### From utility.js
- **Storage** - Local storage management
- **Cookie** - Cookie management
- **Dom** - DOM manipulation
- **Math2** - Math utilities
- **ArrayUtils** - Array operations
- **StringUtils** - String operations
- **DateUtils** - Date formatting and manipulation
- **Logger** - Logging utilities

### From predict.js
- `handlePredictSubmit(e)` - Form submission handler
- `displayPredictionResult(result, inputData)` - Display results
- `resetPredictForm()` - Reset form
- `exportPrediction()` - Export as CSV

### From analyze.js
- `handleAnalyzeSubmit(e)` - Form submission handler
- `previewImage(e)` - Preview uploaded image
- `displayAnalysisResult(result, cropType)` - Display analysis results
- `resetAnalyzeForm()` - Reset form
- `downloadReport()` - Download analysis report
