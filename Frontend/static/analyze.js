// ===============================
// Analyze Page JavaScript
// ===============================

// Disease Treatment Database
const diseaseTreatments = {

    "Pepper__bell__Bacterial_spot": [
        "Remove infected leaves immediately",
        "Apply copper-based bactericide spray",
        "Avoid overhead irrigation",
        "Use disease-free seeds",
        "Practice crop rotation"
    ],

    "Pepper__bell__healthy": [
        "Plant is healthy",
        "Maintain proper watering schedule",
        "Ensure good sunlight exposure",
        "Apply organic fertilizer periodically",
        "Monitor leaves regularly for early symptoms"
    ],

    "Potato__Early_blight": [
        "Apply fungicides such as chlorothalonil or mancozeb",
        "Remove infected leaves and debris",
        "Maintain proper spacing between plants",
        "Use resistant potato varieties",
        "Avoid excessive moisture on leaves"
    ],

    "Potato__healthy": [
        "Plant appears healthy",
        "Maintain balanced soil nutrients",
        "Provide proper irrigation",
        "Ensure good airflow between plants",
        "Regularly inspect plants"
    ],

    "Tomato_Early_blight": [
        "Remove infected leaves immediately",
        "Apply fungicides such as chlorothalonil",
        "Avoid watering leaves directly",
        "Use mulch to prevent soil splash",
        "Rotate crops yearly"
    ],

    "Tomato_Late_blight": [
        "Remove infected plants immediately",
        "Apply fungicides like metalaxyl",
        "Avoid excessive humidity",
        "Ensure proper drainage",
        "Monitor nearby plants regularly"
    ],

    "Tomato_healthy": [
        "Plant is healthy",
        "Maintain consistent watering",
        "Provide sufficient sunlight",
        "Apply balanced fertilizer",
        "Regular monitoring for early disease signs"
    ]
};


// ===============================
// Page Initialization
// ===============================
document.addEventListener("DOMContentLoaded", function () {

    const analyzeForm = document.getElementById("analyzeForm");
    const imageInput = document.getElementById("cropImage");

    if (analyzeForm) {
        analyzeForm.addEventListener("submit", handleAnalyzeSubmit);
    }

    if (imageInput) {
        imageInput.addEventListener("change", previewImage);
    }

});


// ===============================
// Image Preview
// ===============================
function previewImage(e) {

    const file = e.target.files[0];

    if (!file) return;

    const reader = new FileReader();

    reader.onload = function (event) {

        let previewDiv = document.querySelector(".image-preview");

        if (!previewDiv) {
            previewDiv = document.createElement("div");
            previewDiv.className = "image-preview";
            document.getElementById("analyzeForm").parentElement.appendChild(previewDiv);
        }

        previewDiv.innerHTML = `
            <h4>Image Preview:</h4>
            <img src="${event.target.result}" alt="Preview" style="max-width:250px;border-radius:8px;">
        `;

        previewDiv.style.display = "block";
    };

    reader.readAsDataURL(file);

    showNotification("Image loaded successfully", "success");
}


// ===============================
// Analyze Form Submission
// ===============================
async function handleAnalyzeSubmit(e) {

    e.preventDefault();

    const cropType = document.getElementById("cropType").value;
    const imageFile = document.getElementById("cropImage").files[0];

    if (!cropType || !imageFile) {
        showNotification("Please select crop type and image", "warning");
        return;
    }

    if (imageFile.size > 2 * 1024 * 1024) {
        showNotification("Image must be less than 2MB", "error");
        return;
    }

    showLoader();

    const formData = new FormData();
    formData.append("crop_type", cropType);
    formData.append("image", imageFile);

    try {

        const response = await fetch("/api/analyze", {
            method: "POST",
            body: formData
        });

        hideLoader();

        if (!response.ok) {
            showNotification("Analysis failed", "error");
            return;
        }

        const result = await response.json();

        displayAnalysisResult(result, cropType);

        showNotification("Analysis completed successfully", "success");

    } catch (error) {

        hideLoader();
        console.error(error);

        showNotification("Error: " + error.message, "error");
    }
}


// ===============================
// Display Result
// ===============================
function displayAnalysisResult(result, cropType) {

    const resultDiv = document.getElementById("result");

    const hasDisease = result.disease_detected || false;
    const diseaseName = result.disease_name || "Unknown";
    const confidence = result.confidence || 0;

    const treatment = diseaseTreatments[diseaseName] || [
        "Remove infected leaves",
        "Apply appropriate fungicide",
        "Monitor plant health regularly",
        "Ensure proper irrigation",
        "Improve air circulation"
    ];

    const formattedDisease = formatDiseaseName(diseaseName);

    const html = `
        <div class="disease-result" style="border-left:6px solid ${hasDisease ? "#FF9800" : "#4CAF50"};padding:15px;margin-top:20px;border-radius:8px;">
            
            <h3>${hasDisease ? "⚠️ Disease Detected" : "✅ Healthy Plant"}</h3>

            <p><strong>Crop:</strong> ${capitalizeFirstLetter(cropType)}</p>
            <p><strong>Disease:</strong> ${formattedDisease}</p>
            <p><strong>Confidence:</strong> ${(confidence * 100).toFixed(2)}%</p>
            <p><strong>Date:</strong> ${formatDate(new Date())}</p>

            <div class="recommendations">
                <h4>🌿 Recommendations</h4>
                <ul>
                    ${treatment.map(t => `<li>${t}</li>`).join("")}
                </ul>
            </div>

            <button onclick="resetAnalyzeForm()" class="btn-secondary" style="margin-top:15px;">
                Analyze Another Image
            </button>

        </div>
    `;

    resultDiv.innerHTML = html;
    resultDiv.style.display = "block";

    resultDiv.scrollIntoView({ behavior: "smooth" });
}


// ===============================
// Reset Form
// ===============================
function resetAnalyzeForm() {

    document.getElementById("analyzeForm").reset();

    const resultDiv = document.getElementById("result");

    resultDiv.innerHTML = "";
    resultDiv.style.display = "none";

    const preview = document.querySelector(".image-preview");

    if (preview) preview.style.display = "none";
}


// ===============================
// Helper Functions
// ===============================
function capitalizeFirstLetter(text) {
    return text.charAt(0).toUpperCase() + text.slice(1);
}

function formatDiseaseName(name) {
    return name.replace(/_/g, " ");
}

function formatDate(date) {
    return date.toLocaleDateString();
}