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

@app.route('/predict', methods=['POST'])
def predict():
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