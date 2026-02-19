from Backend.exception.exception import Krishmitra
from Backend.logger.logger import logging 
import sys
import os
from flask import Flask,render_template,request,jsonify




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

@app.route('/predict')
def predict_page():
    try:
        return render_template('predict.html')
    except Exception as e:
        raise Krishmitra(e,sys)

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

@app.route('/api/predict', methods=['POST'])
def predict_api():
    data = request.json
    
    temp = data['temperature']
    humidity = data['humidity']

    # Dummy ML logic (replace later)
    result = "High Yield" if temp > 25 else "Low Yield"

    return jsonify({"prediction": result})


if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as e:
        logging.error("Error occurred while running the Flask application: %s", str(e))
        raise Krishmitra(e,sys)