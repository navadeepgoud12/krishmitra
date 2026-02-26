from Backend.logger.logger import logging
from Backend.crop_yield.entity.config_entity import TrainingPipelineConfig,DataInjestionConfig
from Backend.crop_yield.entity.artifacts_entity import DataIngestionArtifact
from Backend.crop_yield.components.data_injestion import DataIngestion
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

    except Exception as e:
        raise Krishmitra(e,sys)