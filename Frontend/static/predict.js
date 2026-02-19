// Predict Page JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const predictForm = document.getElementById('predictForm');
    
    if (predictForm) {
        predictForm.addEventListener('submit', handlePredictSubmit);
    }
});

/**
 * Handle predict form submission
 */
async function handlePredictSubmit(e) {
    e.preventDefault();
    
    // Validate form
    if (!validateForm('predictForm')) {
        showNotification('Please fill all required fields', 'warning');
        return;
    }
    
    // Get form data
    const cropName = document.getElementById('cropName').value;
    const temperature = parseFloat(document.getElementById('temperature').value);
    const humidity = parseFloat(document.getElementById('humidity').value);
    const rainfall = parseFloat(document.getElementById('rainfall').value);
    
    // Validate numeric values
    if (isNaN(temperature) || isNaN(humidity) || isNaN(rainfall)) {
        showNotification('Please enter valid numeric values', 'error');
        return;
    }
    
    showLoader();
    
    // Prepare data
    const data = {
        crop: cropName,
        temperature: temperature,
        humidity: humidity,
        rainfall: rainfall
    };
    
    // Call API
    const result = await apiCall('/api/predict', 'POST', data);
    
    hideLoader();
    
    if (result) {
        displayPredictionResult(result, data);
        showNotification('Prediction completed successfully!', 'success');
    } else {
        showNotification('Failed to get prediction', 'error');
    }
}

/**
 * Display prediction result
 */
function displayPredictionResult(result, inputData) {
    const resultDiv = document.getElementById('result');
    
    // Determine yield quality based on prediction
    let yieldQuality = result.prediction || 'Moderate Yield';
    let yieldColor = '#FF9800';
    
    if (yieldQuality.includes('High')) {
        yieldColor = '#4CAF50';
    } else if (yieldQuality.includes('Low')) {
        yieldColor = '#f44336';
    }
    
    const html = `
        <div class="prediction-result" style="border-left-color: ${yieldColor}; background-color: rgba(76, 175, 80, 0.1);">
            <h4>📊 Prediction Result</h4>
            <p style="font-size: 20px; color: ${yieldColor}; font-weight: 600; margin: 10px 0;">
                ${yieldQuality}
            </p>
            
            <div class="prediction-details">
                <div class="detail-item">
                    <h5>Crop</h5>
                    <p>${capitalizeFirstLetter(inputData.crop)}</p>
                </div>
                <div class="detail-item">
                    <h5>Temperature</h5>
                    <p>${inputData.temperature}°C</p>
                </div>
                <div class="detail-item">
                    <h5>Humidity</h5>
                    <p>${inputData.humidity}%</p>
                </div>
                <div class="detail-item">
                    <h5>Rainfall</h5>
                    <p>${inputData.rainfall}mm</p>
                </div>
            </div>
            
            <div style="margin-top: 20px; padding-top: 20px; border-top: 1px solid #ccc;">
                <h5>Recommendations:</h5>
                <ul style="padding-left: 20px;">
                    <li>Monitor soil moisture regularly</li>
                    <li>Apply fertilizers according to crop requirements</li>
                    <li>Check weather forecasts for next 7 days</li>
                    <li>Prepare for any pest management if needed</li>
                </ul>
            </div>
            
            <button class="btn-secondary" onclick="resetPredictForm()" style="background: #2196F3;">
                Make Another Prediction
            </button>
        </div>
    `;
    
    resultDiv.innerHTML = html;
    resultDiv.style.display = 'block';
    resultDiv.scrollIntoView({ behavior: 'smooth' });
}

/**
 * Reset predict form
 */
function resetPredictForm() {
    document.getElementById('predictForm').reset();
    document.getElementById('result').innerHTML = '';
    document.getElementById('result').style.display = 'none';
}

/**
 * Export prediction as CSV
 */
function exportPrediction() {
    const cropName = document.getElementById('cropName').value;
    const temperature = document.getElementById('temperature').value;
    const humidity = document.getElementById('humidity').value;
    const rainfall = document.getElementById('rainfall').value;
    
    const csv = `Crop,Temperature,Humidity,Rainfall,Prediction Date\n${cropName},${temperature},${humidity},${rainfall},${new Date().toLocaleDateString()}`;
    
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `prediction_${Date.now()}.csv`;
    a.click();
    
    showNotification('Prediction exported successfully', 'success');
}
