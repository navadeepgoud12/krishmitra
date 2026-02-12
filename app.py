from flask import Flask
from exception.exception import Krishmitra
from logging.logger import logging
import sys
import os
from flask import render_template


app = Flask(__name__)

@app.route('/')
def home():
    try:
        return render_template('home.html')
    except Exception as e:
        raise Krishmitra(e,sys)



if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as e:
        logging.error("Error occurred while running the Flask application: %s", str(e))
        raise Krishmitra(e,sys)