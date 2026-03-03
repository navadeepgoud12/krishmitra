// Predict Page JavaScript (Final Working Version)
console.log("Predict JS Loaded 🚀");

document.addEventListener("DOMContentLoaded", function () {

    console.log("Predict JS loaded ✅");

    const form = document.getElementById("predictForm");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        console.log("Form submitted ✅");

        // Collect form data
        const data = {
            Crop: document.querySelector("[name='Crop']").value,
            Crop_Year: document.querySelector("[name='Crop_Year']").value,
            Season: document.querySelector("[name='Season']").value,
            State: document.querySelector("[name='State']").value,
            Area: document.querySelector("[name='Area']").value,
            Annual_Rainfall: document.querySelector("[name='Annual_Rainfall']").value,
            Fertilizer: document.querySelector("[name='Fertilizer']").value,
            Pesticide: document.querySelector("[name='Pesticide']").value,
            Avg_Temperature: document.querySelector("[name='Avg_Temperature']").value,
            Max_Temperature: document.querySelector("[name='Max_Temperature']").value,
            Min_Temperature: document.querySelector("[name='Min_Temperature']").value
        };

        console.log("Sending data:", data);

        try {
            const response = await fetch("/api/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            console.log("Server response:", result);

            if (!response.ok) {
                alert(result.error || "Server error occurred");
                return;
            }

            displayResult(result.prediction);

        } catch (error) {
            console.error("Error:", error);
            alert("Network error. Check console.");
        }
    });

});


function displayResult(prediction) {

    console.log("Displaying result:", prediction);

    const resultDiv = document.getElementById("result");

    resultDiv.innerHTML = `
        <div style="
            margin-top: 25px;
            padding: 20px;
            background: #e8f5e9;
            border-left: 6px solid #2e7d32;
            border-radius: 10px;
            font-size: 22px;
            font-weight: bold;
            color: #2e7d32;
        ">
            🌾 Predicted Yield: ${prediction}
        </div>
    `;

    resultDiv.style.display = "block";
}