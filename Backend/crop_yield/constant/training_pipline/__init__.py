import pandas as pd
import numpy as np
import os
import sys

"""
defining some constant variables for training pipeline
"""
TARGET_COLUMN:str = "Result"
PIPELINE_NAME:str = "Krishmitra"
ARTIFACT_DIR:str = "Artifacts"
FILE_NAME:str = "cropdata.csv"
TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

"""
 data injestion related constant start with DATA_INJESTION var name
"""

DATA_INJESTION_COLLECTION_NAME:str = "Cropyield"
DATA_INJESTION_DATABASE_NAME:str = "KrishMitra"
DATA_INJESTION_DIR_NAME:str = "data_injestion"
DATA_INJESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INJESTION_INGESTED_DIR:str = "ingested"
DATA_INJESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2