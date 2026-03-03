from Backend.exception.exception import Krishmitra
from Backend.logger.logger import logging 
import sys
import os
from flask import Flask,render_template,request,jsonify
import numpy as np
import pandas as pd
from Backend.crop_yield.utils.main_utils import load_object

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

        input_dict = {
            "Crop": data["Crop"],
            "Crop_Year": float(data["Crop_Year"]),
            "Season": data["Season"],
            "State": data["State"],
            "Area": float(data["Area"]),
            "Annual_Rainfall": float(data["Annual_Rainfall"]),
            "Fertilizer": float(data["Fertilizer"]),
            "Pesticide": float(data["Pesticide"]),
            "Avg_Temperature": float(data["Avg_Temperature"]),
            "Max_Temperature": float(data["Max_Temperature"]),
            "Min_Temperature": float(data["Min_Temperature"]),
        }

        input_df = pd.DataFrame([input_dict])

        prediction = model.predict(input_df)
        result = round(prediction[0], 2)

        return jsonify({
            "prediction": result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400



if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as e:
        logging.error("Error occurred while running the Flask application: %s", str(e))
        raise Krishmitra(e,sys)