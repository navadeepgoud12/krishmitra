from Backend.disease_prediction.components.data_ingestion import DataIngestion
from Backend.disease_prediction.components.data_validation import DataValidation
from Backend.disease_prediction.components.data_transformation import DataTransformation
from Backend.disease_prediction.components.model_trainer import ModelTrainer
import os,sys
from Backend.exception.exception import Krishmitra
from Backend.logger.logger import logging
def start_training():
    try:
        logging.info("data ingestion in disease prediction started")
        ingestion = DataIngestion()
        ingestion.split_dataset()
        logging.info("data inestion is completed")
        logging.info("data validation has started")
        validation = DataValidation("artifacts/train")
        validation.validate()
        logging.info("data validation is completed")
        logging.info("data transformation has been started")
        

        transform = DataTransformation()
        train_data, test_data = transform.transform()
        logging.info("data transformation completed")
        logging.info("model traing started")

        trainer = ModelTrainer()
        trainer.train(train_data, test_data)
        logging.info("model trainging completed")
    except Exception as e:
        raise Krishmitra(e,sys)


if __name__ == "__main__":
    start_training()