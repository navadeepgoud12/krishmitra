import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URI")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from Backend.exception.exception import Krishmitra
from Backend.logger.logger import logging

class KrishMitraDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise Krishmitra(e,sys)
        
    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise Krishmitra(e,sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL,
                tls=True,
                tlsCAFile=certifi.where(),
                tlsAllowInvalidCertificates=True,
                retryWrites=False,
                serverSelectionTimeoutMS=60000,
                connectTimeoutMS=60000,
                socketTimeoutMS=60000,
                maxPoolSize=1
            )
            print(f"✓ Connected to MongoDB")
            self.database = self.mongo_client[self.database]
            
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise Krishmitra(e,sys)
        
if __name__=='__main__':
    FILE_PATH = os.path.join("data", "cropdata.csv")
    DATABASE="KrishMitra"
    Collection="Cropyield"
    networkobj=KrishMitraDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)