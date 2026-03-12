from Backend.exception.exception import Krishmitra
from Backend.logger.logger import logging 
import sys
import os
from flask import Flask,render_template,request,jsonify
import numpy as np
import pandas as pd
from Backend.crop_yield.utils.main_utils import load_object
from Backend.disease_prediction.predict import predict_disease
import cv2
from dotenv import load_dotenv
load_dotenv()


model = load_object("final_model/model.pkl")

# Try to load preprocessor, create a simple mapping if not available
try:
    preprocessor = load_object("final_model/preprocessor.pkl")
except:
    preprocessor = None



import os

from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder='Frontend/templates',
    static_folder='Frontend/static'
)


@app.route('/')
def home():
    try:
        return render_template('home.html')
    except Exception as e:
        raise Krishmitra(e,sys)


@app.route("/predict")
def predict():
    try:
        # GET request - just show the form
        if request.method == "GET":
            return render_template("predict.html")
        
        

    except Exception as e:
        return str(e)

@app.route('/analyze')
def analyze():
    try:
        return render_template('analyze.html')
    except Exception as e:
        raise Krishmitra(e,sys)

@app.route('/weather')
def weather():
    try:
        return render_template('weather.html')
    except Exception as e:
        raise Krishmitra(e,sys)

@app.route('/market')
def market():
    try:
        return render_template('market.html')
    except Exception as e:
        raise Krishmitra(e,sys)

@app.route('/schemes')
def schemes():
    try:
        return render_template('schemes.html')
    except Exception as e:
        raise Krishmitra(e,sys)
    
@app.route("/api/predict", methods=["POST"])
def api_predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        print("Incoming Data:", data)   # DEBUG

        input_dict = {
            "Crop": data.get("Crop"),
            "Crop_Year": float(data.get("Crop_Year", 0)),
            "Season": data.get("Season"),
            "State": data.get("State"),
            "Area": float(data.get("Area", 0)),
            "Annual_Rainfall": float(data.get("Annual_Rainfall", 0)),
            "Fertilizer": float(data.get("Fertilizer", 0)),
            "Pesticide": float(data.get("Pesticide", 0)),
            "Avg_Temperature": float(data.get("Avg_Temperature", 0)),
            "Max_Temperature": float(data.get("Max_Temperature", 0)),
            "Min_Temperature": float(data.get("Min_Temperature", 0)),
        }

        input_df = pd.DataFrame([input_dict])

        prediction = model.predict(input_df)

        result = float(round(prediction[0], 2))

        return jsonify({
            "prediction": result
    })
    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 400

@app.route("/predict_disease", methods=["POST"])
def predict_disease_route():
    try:

        # Disease Treatment Database
        disease_treatments = {

            "Pepper__bell__Bacterial_spot": [
                "Remove infected leaves",
                "Apply copper-based bactericide",
                "Avoid overhead irrigation",
                "Use disease-free seeds",
                "Practice crop rotation"
            ],

            "Pepper__bell__healthy": [
                "Plant is healthy",
                "Maintain proper watering",
                "Ensure adequate sunlight",
                "Apply organic fertilizer",
                "Monitor leaves regularly"
            ],

            "Potato__Early_blight": [
                "Apply fungicide such as mancozeb",
                "Remove infected plant debris",
                "Ensure proper airflow",
                "Use resistant varieties",
                "Avoid excessive moisture"
            ],

            "Potato__healthy": [
                "Maintain proper irrigation",
                "Ensure balanced nutrients",
                "Monitor leaves regularly",
                "Keep soil well drained",
                "Use preventive care"
            ],

            "Tomato_Early_blight": [
                "Apply chlorothalonil fungicide",
                "Remove infected leaves",
                "Use mulch to prevent soil splash",
                "Rotate crops yearly",
                "Avoid watering leaves"
            ],

            "Tomato_Late_blight": [
                "Remove infected plants immediately",
                "Apply metalaxyl fungicide",
                "Improve drainage",
                "Avoid humidity buildup",
                "Monitor nearby plants"
            ],

            "Tomato_healthy": [
                "Maintain proper watering",
                "Provide enough sunlight",
                "Apply balanced fertilizer",
                "Inspect plants regularly",
                "Ensure proper airflow"
            ]
        }

        # Get uploaded image
        file = request.files["leaf_image"]

        upload_folder = "Frontend/static/uploads"
        os.makedirs(upload_folder, exist_ok=True)

        filepath = os.path.join(upload_folder, file.filename)
        file.save(filepath)

        # Predict disease
        disease = predict_disease(filepath)

        # Get recommendations
        solution = disease_treatments.get(disease, ["No recommendation available"])

        # Format disease name (remove underscores)
        formatted_disease = disease.replace("_", " ")

        return render_template(
            "analyze.html",
            disease=formatted_disease,
            solution=solution,
            image=file.filename
        )

    except Exception as e:
        return str(e)
import requests

import requests

import requests

@app.route("/api/weather")
def get_weather():

    city = "Hyderabad"
    api_key = os.getenv("WEATHER_API_KEY")

    current_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

    current = requests.get(current_url).json()
    forecast = requests.get(forecast_url).json()

    # collect next 24 hours temperatures
    temps = [item["main"]["temp"] for item in forecast["list"][:8]]

    max_temp = max(temps)
    min_temp = min(temps)
    avg_temp = round(sum(temps) / len(temps), 2)

    data = {
        "temp": current["main"]["temp"],
        "humidity": current["main"]["humidity"],
        "wind": current["wind"]["speed"],
        "condition": current["weather"][0]["main"],

        "forecast": [
            forecast["list"][8]["main"]["temp"],
            forecast["list"][16]["main"]["temp"],
            forecast["list"][24]["main"]["temp"]
        ],

        "max_temp": max_temp,
        "min_temp": min_temp,
        "avg_temp": avg_temp
    }

    return data


if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as e:
        logging.error("Error occurred while running the Flask application: %s", str(e))
        raise Krishmitra(e,sys)