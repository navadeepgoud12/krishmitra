import os,sys
from Backend.exception.exception import Krishmitra
from Backend.logger.logger import logging

class DataValidation:

    def __init__(self, train_path):
        self.train_path = train_path

    def validate(self):
        try:
            if not os.path.exists(self.train_path):
                raise Exception("Training data not found")

            classes = os.listdir(self.train_path)

            if len(classes) < 2:
                raise Exception("Not enough classes")

            print("Data Validation Passed")
        except Exception as e:
            raise Krishmitra(e,sys)