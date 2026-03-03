import os
import sys

from Backend.exception.exception import Krishmitra
from Backend.logger.logger import logging
from Backend.crop_yield.components.data_injestion import DataIngestion
from Backend.crop_yield.components.data_validation import DataValidation
from Backend.crop_yield.components.data_transformation import DataTransformation
from Backend.crop_yield.components.model_trainer import ModelTrainer

from Backend.crop_yield.entity.config_entity import(
    TrainingPipelineConfig,
    DataInjestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
)

from Backend.crop_yield.entity.artifacts_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact,
)


class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
    def start_data_ingestion(self):

        try:
            self.data_ingestion_config = DataInjestionConfig(training_pipeline_config= self.training_pipeline_config)
            logging.info("start datainjestion")
            data_injestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_injestion_artifact = data_injestion.initiate_data_ingestion()
            logging.info(f"data injestion is completed and artifact {data_injestion_artifact}")

            return data_injestion_artifact

        except Exception as e:
            raise Krishmitra(e,sys)
        
    
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact):
        try:
            
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("data validation is started ")
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,data_validation_config=data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info(f"data validation is completed and artifact is {data_validation_artifact}")

            return data_validation_artifact

        except Exception as e:

            raise Krishmitra(e,sys)
        

    def start_data_transformation(self,data_valiadtion_artifact:DataValidationArtifact):
        try:
            data_transformation_config = DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("data_transformation is started")
            data_transformation = DataTransformation(data_validation_artifact=data_valiadtion_artifact,data_transformation_config=data_transformation_config)
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            logging.info(f"data transformation is completed {data_transformation_artifact}")

            return data_transformation_artifact
            
        except Exception as e:
            raise Krishmitra(e,sys)
        

    def start_model_trainer(self,data_transformation_artifact:DataTransformationArtifact)->ModelTrainerArtifact:
        try:
            self.model_trainer_config: ModelTrainerConfig = ModelTrainerConfig(
                training_pipeline_config=self.training_pipeline_config
            )

            model_trainer = ModelTrainer(
                data_transformation_artifact=data_transformation_artifact,
                model_trainer_config=self.model_trainer_config,
            )

            model_trainer_artifact = model_trainer.initate_model_trainer()

            return model_trainer_artifact

        except Exception as e:
            raise Krishmitra(e, sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact=self.start_data_transformation(data_valiadtion_artifact=data_validation_artifact)
            model_trainer_artifact=self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            
            
            return model_trainer_artifact
        except Exception as e:
            raise Krishmitra(e,sys)