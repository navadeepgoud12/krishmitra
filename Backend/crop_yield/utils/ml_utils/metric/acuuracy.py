from Backend.exception.exception import Krishmitra
from Backend.logger.logger import logging
from Backend.crop_yield.entity.artifacts_entity import AccuracyArtifact
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,accuracy_score

import os,sys



def get_score(y_true,y_pred)->AccuracyArtifact:
    try:
            
        model_mean_squared_error = mean_squared_error(y_true, y_pred)
        model_mean_absolute_error = mean_absolute_error(y_true, y_pred)
        model_r2_score = r2_score(y_true,y_pred)


        accuracy_score_metric =  AccuracyArtifact(mean_squared_error=model_mean_squared_error,
                mean_absolute_error=model_mean_absolute_error, 
                r2_score=model_r2_score)
        return accuracy_score_metric
    except Exception as e:
        raise Krishmitra(e,sys)