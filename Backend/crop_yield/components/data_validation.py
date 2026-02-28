
from Backend.crop_yield.entity.artifacts_entity import DataIngestionArtifact,DataValidationArtifact
from Backend.crop_yield.entity.config_entity import DataValidationConfig
from Backend.exception.exception import Krishmitra
from Backend.logger.logger import logging
from Backend.crop_yield.constant.training_pipline import SCHEMA_FILE_PATH

from scipy.stats import ks_2samp
import os
import sys
import pandas as pd
import numpy as np
from Backend.crop_yield.utils.main_utils import read_yaml_file,write_yaml_file

class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise Krishmitra(e,sys)
    
    #static method is used when we want to define a method that does not depend on the instance of the class. It can be called on the class itself, rather than on an instance of the class. 
    # Static methods are defined using the @staticmethod decorator and do not take the self parameter as their first argument. They are typically used for utility functions that perform a specific task and do not require access to instance variables or methods.
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise Krishmitra(e,sys)

    def validate_number_of_columns(self,dataframe:pd.DataFrame)->bool:
        try:
            number_of_columns = len(self._schema_config["columns"])
            logging.info(f"number of columns in the schema: {number_of_columns}")
            logging.info(f"number of columns in the dataframe: {len(dataframe.columns)}")

            if len(dataframe.columns) == number_of_columns:
                return True
            return False
        except Exception as e:
            raise Krishmitra(e,sys)
        
    def numeric_columns_exist(self,dataframe:pd.DataFrame)->bool:
            try:
                numeric_columns = self._schema_config["numeric_columns"]
                logging.info(f"numeric columns in the schema: {numeric_columns}")
                numeric_columns_in_dataframe = [column for column in dataframe.columns if column in numeric_columns]
                logging.info(f"numeric columns in the dataframe: {numeric_columns_in_dataframe}")

                if len(numeric_columns_in_dataframe) == len(numeric_columns):
                    return True
                return False
            except Exception as e:
                raise Krishmitra(e,sys)

    def detect_dataset_drift(self,base_df,current_df,threshold=0.05)->bool:
        try:
            status = True
            report = {}
            for column in base_df.columns:
                d1 = base_df[column]
                d2 = current_df[column]
                is_sample_dist = ks_2samp(d1,d2)
                if is_sample_dist.pvalue > threshold:
                    is_found = False
                else:
                    is_found = True
                    status = False
                report.update({column:{
                    "p_value":float(is_sample_dist.pvalue),
                    "drift_status":is_found
                }})
            drift_report_file_path = self.data_validation_config.drift_report_file_path
            # create directory
            dir_path = os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path,exist_ok=True)
            write_yaml_file(file_path=drift_report_file_path,content=report)
            return status
        except Exception as e:
            raise Krishmitra(e,sys)

    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
            # read the train and test data
            train_dataframe = DataValidation.read_data(train_file_path)
            test_dataframe = DataValidation.read_data(test_file_path)

            # validating the number of columns in train and test data
            logging.info("validating training and testing data for number of columns")

            status = self.validate_number_of_columns(train_dataframe)
            if not status:
                error_message = f"number of columns in the training data is not equal to the number of columns in the schema file"
            status = self.validate_number_of_columns(test_dataframe)
            if not status:
                error_message = f"number of columns in the testing data is not equal to the number of columns in the schema file"
            
            # validating the numeric columns in train and test data
            logging.info("validating training and testing data for numeric columns")

            status = self.numeric_columns_exist(train_dataframe)
            if not status:
                error_message = f"numeric columns in the training data are not present in the schema file"
            status = self.numeric_columns_exist(test_dataframe)
            if not status:
                error_message = f"numeric columns in the testing data are not present in the schema file"

            #lets check data drift 
            status = self.detect_dataset_drift(base_df=train_dataframe,current_df=test_dataframe)
            dir_path = os.path.dirname(self.data_validation_config.valid_train_file_path)
            os.makedirs(dir_path,exist_ok=True)

            train_dataframe.to_csv(self.data_validation_config.valid_train_file_path,index=False,header=True)
            test_dataframe.to_csv(self.data_validation_config.valid_test_file_path,index=False,header=True)

            data_validation_artifact = DataValidationArtifact(
                validation_status=status,
                valid_train_file_path=self.data_validation_config.valid_train_file_path,
                valid_test_file_path=self.data_validation_config.valid_test_file_path,
                invalid_train_file_path=None,
                invalid_test_file_path=None,
                drift_report_file_path=self.data_validation_config.drift_report_file_path,
            )
                
            return data_validation_artifact



        except Exception as e:
            raise Krishmitra(e,sys)
