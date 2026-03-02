from Backend.logger.logger import logging
from Backend.crop_yield.entity.config_entity import TrainingPipelineConfig,DataInjestionConfig,DataValidationConfig,DataTransformationConfig
from Backend.crop_yield.entity.artifacts_entity import DataIngestionArtifact
from Backend.crop_yield.components.data_injestion import DataIngestion
from Backend.crop_yield.components.data_validation import DataValidation
from Backend.crop_yield.components.data_transformation import DataTransformation
from Backend.exception.exception import Krishmitra

import os
import sys

if __name__ == "__main__":
    try:
        TrainingPipelineConfig = TrainingPipelineConfig()
        datainjestionconfig = DataInjestionConfig(TrainingPipelineConfig)
        data_ingestion = DataIngestion(datainjestionconfig)
        logging.info("Starting data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info(f"Data ingestion completed and artifact is {dataingestionartifact}")
        data_validation_config = DataValidationConfig(TrainingPipelineConfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        logging.info("initate the data valiadtion")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info(f"Data validation completed and artifact is {data_validation_artifact}")
        print(data_validation_artifact)
        data_transformation_config = DataTransformationConfig(TrainingPipelineConfig)
        logging.info("data transformation has been started.")
        data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact =  data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info(f"data transformation completed and artifact is {data_transformation_artifact}")

    except Exception as e:
        raise Krishmitra(e,sys)