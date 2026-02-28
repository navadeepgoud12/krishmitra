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

SCHEMA_FILE_PATH = "Backend\data_schema\schema.yaml"

"""
 data injestion related constant start with DATA_INJESTION var name
"""

DATA_INJESTION_COLLECTION_NAME:str = "Cropyield"
DATA_INJESTION_DATABASE_NAME:str = "KrishMitra"
DATA_INJESTION_DIR_NAME:str = "data_injestion"
DATA_INJESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INJESTION_INGESTED_DIR:str = "ingested"
DATA_INJESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2

""" Data validation related constant start with DATA_VALIDATION var name"""
DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_VALID_DIR:str = "validated"
DATA_VALIDATION_INVALID_DIR:str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str = "report.yaml"