from Backend.exception.exception import Krishmitra
from Backend.logger.logger import logging

#configuration of the data ingestion component

from Backend.crop_yield.entity.config_entity import DataInjestionConfig

from Backend.crop_yield.entity.artifacts_entity import DataIngestionArtifact

import os
import sys
import pymongo
import pandas as pd
import numpy as np
from typing import List
from sklearn.model_selection import train_test_split
import certifi

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URI")


class DataIngestion:
    """
    read data from mongo db and store it in feature store and ingested dir

    """
    def __init__(self,data_ingestion_config:DataInjestionConfig):
        
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise Krishmitra(e,sys)
        
    def collection_as_dataframe(self):
        """

        reading data from the mongodb and converting it into dataframe and replacing the na values with np.nan
        """
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop("_id",axis=1)

            df.replace({"na":np.nan},inplace=True)

            return df

        except Exception as e:
            raise Krishmitra(e,sys)
        
    def export_data_into_feature_store(self,dataframe:pd.DataFrame):
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            #creating the directory for feature store if not exist
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)

            return dataframe
        except Exception as e:
            raise Krishmitra(e,sys)
    
    def split_data_as_train_test(self,dataframe:pd.DataFrame):
        """
        Docstring for split_data_as_train_test
        
        :param self: Description
        :param dataframe: Description
        :type dataframe: pd.DataFrame

        splitting the data into train and test set and exporting it to the ingested dir means the data which is ingested into the training pipeline
        """
        try:
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ratio
            )
            logging.info(f"splitting the data into train and test set with test size {self.data_ingestion_config.train_test_split_ratio}")
            logging.info(f"exited the split_data_as_train_test method of DataIngestion class")

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(f"exporting the train and test file to path: {self.data_ingestion_config.training_file_path} and {self.data_ingestion_config.testing_file_path}")
            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)

            logging.info("exported the train and test file successfully")
        except Exception as e:
            raise Krishmitra(e,sys)
    def initiate_data_ingestion(self):
        try:
            dataframe = self.collection_as_dataframe()
            dataframe = self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            dataingestionartifact = DataIngestionArtifact(train_file_path=self.data_ingestion_config.training_file_path,
                                                          test_file_path=self.data_ingestion_config.testing_file_path)
            
            return dataingestionartifact
        except Exception as e:
            raise Krishmitra(e,sys)