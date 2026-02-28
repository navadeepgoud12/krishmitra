import os
import sys
from datetime import datetime

from Backend.crop_yield.constant import training_pipline

print(training_pipline.ARTIFACT_DIR)
print(training_pipline.PIPELINE_NAME)


class TrainingPipelineConfig:
    def __init__(self,timestamp = datetime.now()):
        self.timestamp = timestamp.strftime("%m-%d-%Y-%H-%M-%S")
        self.pipeline_name = training_pipline.PIPELINE_NAME
        self.artifact_name = training_pipline.ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name,self.timestamp)
        self.timestamp:str = timestamp

class DataInjestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir:str=os.path.join(
            training_pipeline_config.artifact_dir,training_pipline.DATA_INJESTION_DIR_NAME
        )
        self.feature_store_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipline.DATA_INJESTION_FEATURE_STORE_DIR, training_pipline.FILE_NAME
            )
        self.training_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipline.DATA_INJESTION_INGESTED_DIR, training_pipline.TRAIN_FILE_NAME
            )
        self.testing_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipline.DATA_INJESTION_INGESTED_DIR, training_pipline.TEST_FILE_NAME
            )
        self.train_test_split_ratio: float = training_pipline.DATA_INJESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name: str = training_pipline.DATA_INJESTION_COLLECTION_NAME
        self.database_name: str = training_pipline.DATA_INJESTION_DATABASE_NAME
    
class DataValidationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir:str = os.path.join(training_pipeline_config.artifact_dir,training_pipline.DATA_VALIDATION_DIR_NAME)
        self.valid_data_dir:str = os.path.join(self.data_validation_dir,training_pipline.DATA_VALIDATION_VALID_DIR)
        self.invalid_data_dir:str = os.path.join(self.data_validation_dir,training_pipline.DATA_VALIDATION_INVALID_DIR)
        # valid data file path
        self.valid_train_file_path:str = os.path.join(self.valid_data_dir,training_pipline.TRAIN_FILE_NAME)
        self.valid_test_file_path:str = os.path.join(self.valid_data_dir,training_pipline.TEST_FILE_NAME)
        #invalid data file path
        self.invalid_train_data_dir:str = os.path.join(self.invalid_data_dir,training_pipline.TRAIN_FILE_NAME)
        self.invalid_test_data_dir:str = os.path.join(self.invalid_data_dir,training_pipline.TEST_FILE_NAME)
        self.drift_report_file_path:str = os.path.join(self.data_validation_dir,training_pipline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)