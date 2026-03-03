from Backend.crop_yield.constant.training_pipline import SAVED_MODEL_DIR,MODEL_FILE_NAME
from Backend.exception.exception import Krishmitra
from Backend.logger.logger import logging

import os,sys

class KrishmitraModel:
    def __init__(self,preprocessor,model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise Krishmitra(e,sys)
    
    def predict(self,x):
        try:
            x_transform = self.preprocessor.transform(x)
            y_hat = self.model.predict(x_transform)
            return y_hat
        except Exception as e:
            raise Krishmitra(e,sys)