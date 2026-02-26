// Analyze Page JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const analyzeForm = document.getElementById('analyzeForm');
    const imageInput = document.getElementById('cropImage');
    
    if (analyzeForm) {
        analyzeForm.addEventListener('submit', handleAnalyzeSubmit);
    }
    
    if (imageInput) {
        imageInput.addEventListener('change', previewImage);
    }
});

/**
 * Preview image before upload
 */
function previewImage(e) {
    const file = e.target.files[0];
    
    if (file) {
        const reader = new FileReader();
        
        reader.onload = function(event) {
            const imagePreview = document.querySelector('.image-preview');
            
            if (!imagePreview) {
                const preview = document.createElement('div');
                preview.className = 'image-preview';
                document.getElementById('analyzeForm').parentElement.appendChild(preview);
            }
            
            document.querySelector('.image-preview').innerHTML = `
                <h4>Image Preview:</h4>
                <img src="${event.target.result}" alt="Preview">
            `;
            document.querySelector('.image-preview').style.display = 'block';
        };
        
        reader.readAsDataURL(file);
        showNotification('Image loaded successfully', 'success');
    }
}

/**
 * Handle analyze form submission
 */
async function handleAnalyzeSubmit(e) {
    e.preventDefault();
    
    const cropType = document.getElementById('cropType').value;
    const imageFile = document.getElementById('cropImage').files[0];
    
    if (!cropType || !imageFile) {
        showNotification('Please fill all fields and select an image', 'warning');
        return;
    }
    
    // Validate file size (max 2MB)
    if (imageFile.size > 2 * 1024 * 1024) {
        showNotification('Image size should be less than 2MB', 'error');
        return;
    }
    
    showLoader();
    
    // Create FormData for file upload
    const formData = new FormData();
    formData.append('crop_type', cropType);
    formData.append('image', imageFile);
    
    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            body: formData
        });
        
        hideLoader();
        
        if (response.ok) {
            const result = await response.json();
            displayAnalysisResult(result, cropType);
            showNotification('Analysis completed successfully!', 'success');
        } else {
            showNotification('Analysis failed. Please try again.', 'error');
        }
    } catch (error) {
        hideLoader();
        console.error('Error:', error);
        showNotification('Error: ' + error.message, 'error');
    }
}

/**
 * Display analysis result
 */
function displayAnalysisResult(result, cropType) {
    const resultDiv = document.getElementById('result');
    
    const hasDisease = result.disease_detected || false;
    const diseaseName = result.disease_name || 'Unknown';
    const confidence = result.confidence || 0;
    const treatment = result.treatment || [];
    
    const html = `
        <div class="disease-result" style="border-left-color: ${hasDisease ? '#FF9800' : '#4CAF50'};">
            <h4>${hasDisease ? '⚠️ Disease Detected' : '✅ Healthy Plant'}</h4>
            
            <div class="disease-info">
                <p><strong>Crop Type:</strong> ${capitalizeFirstLetter(cropType)}</p>
                ${hasDisease ? `<p><strong>Disease:</strong> ${diseaseName}</p>` : ''}
                <p><strong>Confidence:</strong> ${(confidence * 100).toFixed(2)}%</p>
                <p><strong>Analysis Date:</strong> ${formatDate(new Date())}</p>
            </div>
            
            ${hasDisease ? `
                <div class="recommendations">
                    <h5>🌿 Treatment Recommendations:</h5>
                    <ul>
                        ${treatment.length > 0 ? treatment.map(t => `<li>${t}</li>`).join('') : `
                            <li>Isolate affected plants</li>
                            <li>Apply appropriate fungicide/pesticide</li>
                            <li>Improve drainage and reduce humidity</li>
                            <li>Remove infected leaves</li>
                            <li>Monitor other plants regularly</li>
                        `}
                    </ul>
                </div>
            ` : `
                <div class="recommendations">
                    <h5>✨ Plant Health Status:</h5>
                    <ul>
                        <li>Plant appears healthy</li>
                        <li>Continue regular monitoring</li>
                        <li>Maintain proper irrigation schedule</li>
                        <li>Ensure adequate sunlight exposure</li>
                        <li>Apply preventative measures regularly</li>
                    </ul>
                </div>
            `}
            
            <button class="btn-secondary" onclick="resetAnalyzeForm()" style="background: #2196F3;">
                Analyze Another Image
            </button>
        </div>
    `;
    
    resultDiv.innerHTML = html;
    resultDiv.style.display = 'block';
    resultDiv.scrollIntoView({ behavior: 'smooth' });
}

/**
 * Reset analyze form
 */
function resetAnalyzeForm() {
    document.getElementById('analyzeForm').reset();
    document.getElementById('result').innerHTML = '';
    document.getElementById('result').style.display = 'none';
    
    const imagePreview = document.querySelector('.image-preview');
    if (imagePreview) {
        imagePreview.style.display = 'none';
    }
}

/**
 * Download analysis report
 */
function downloadReport() {
    const reportContent = `
CROP DISEASE ANALYSIS REPORT
============================
Generated: ${formatDate(new Date())}

Analysis Details:
- Crop Type: ${document.getElementById('cropType').value}
- Status: Complete
- File: Analysis Report

Recommendations: Check the disease detection report for detailed treatment options.
    `;
    
    const blob = new Blob([reportContent], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `analysis_report_${Date.now()}.txt`;
    a.click();
    
    showNotification('Report downloaded successfully', 'success');
}
