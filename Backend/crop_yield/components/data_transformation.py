import sys
import numpy as np
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.impute import KNNImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from Backend.exception.exception import Krishmitra
from Backend.logger.logger import logging

from Backend.crop_yield.entity.artifacts_entity import DataTransformationArtifact, DataValidationArtifact
from Backend.crop_yield.entity.config_entity import DataTransformationConfig

from Backend.crop_yield.constant.training_pipline import TARGET_COLUMN
from Backend.crop_yield.utils.main_utils import save_numpy_array_data, save_object


class DataTransformation:
    def __init__(self,
                 data_validation_artifact: DataValidationArtifact,
                 data_transformation_config: DataTransformationConfig):

        try:
            self.data_validation_artifact = data_validation_artifact
            self.data_transformation_config = data_transformation_config
            logging.info("Data Transformation initialized")
        except Exception as e:
            raise Krishmitra(e, sys)

    # ============================
    # Read Data
    # ============================
    @staticmethod
    def read_data(file_path: str) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise Krishmitra(e, sys)

    # ============================
    # Outlier Fit (IQR)
    # ============================
    def fit_outlier_bounds(self, df):
        bounds = {}
        num_cols = df.select_dtypes(include=np.number).columns

        for col in num_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1

            # skip constant columns
            if IQR == 0:
                continue

            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            if lower < upper:
                bounds[col] = (lower, upper)

        return bounds

    # ============================
    # Apply Outlier Clipping
    # ============================
    def apply_outlier_bounds(self, df, bounds):
        for col, (lower, upper) in bounds.items():
            df[col] = df[col].clip(lower, upper)
        return df

    # ============================
    # Preprocessor
    # ============================
    def get_preprocessor(self, df: pd.DataFrame):
        try:
            num_features = df.select_dtypes(include=np.number).columns.tolist()
            cat_features = df.select_dtypes(exclude=np.number).columns.tolist()

            if len(num_features) == 0:
                raise Exception("No numerical columns found")

            if len(cat_features) == 0:
                raise Exception("No categorical columns found")

            logging.info(f"NUM columns: {num_features}")
            logging.info(f"CAT columns: {cat_features}")

            num_pipeline = Pipeline([
                ("imputer", KNNImputer(n_neighbors=3)),
                ("scaler", StandardScaler())
            ])

            cat_pipeline = Pipeline([
                ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
            ])

            preprocessor = ColumnTransformer([
                ("num", num_pipeline, num_features),
                ("cat", cat_pipeline, cat_features)
            ])

            return preprocessor

        except Exception as e:
            raise Krishmitra(e, sys)

    # ============================
    # MAIN FUNCTION
    # ============================
    def initiate_data_transformation(self) -> DataTransformationArtifact:
        try:
            logging.info("Data Transformation started")

            train_df = self.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df = self.read_data(self.data_validation_artifact.valid_test_file_path)

            # ============================
            # TARGET SPLIT
            # ============================
            X_train = train_df.drop(columns=[TARGET_COLUMN, "Production"], errors="ignore")
            y_train = train_df[TARGET_COLUMN]

            X_test = test_df.drop(columns=[TARGET_COLUMN, "Production"], errors="ignore")
            y_test = test_df[TARGET_COLUMN]

            # ============================
            # LOG TRANSFORMATION
            # ============================
            log_cols = ["Area", "Fertilizer", "Pesticide"]

            for col in log_cols:
                if col in X_train.columns:
                    X_train[col] = np.log1p(X_train[col])
                    X_test[col] = np.log1p(X_test[col])

            # ============================
            # OUTLIER HANDLING
            # ============================
            bounds = self.fit_outlier_bounds(X_train)

            X_train = self.apply_outlier_bounds(X_train, bounds)
            X_test = self.apply_outlier_bounds(X_test, bounds)

            # ============================
            # PREPROCESSING
            # ============================
            preprocessor = self.get_preprocessor(X_train)

            X_train_transformed = preprocessor.fit_transform(X_train)
            X_test_transformed = preprocessor.transform(X_test)

            # ============================
            # FINAL ARRAY (SAFE)
            # ============================
            y_train = np.array(y_train).reshape(-1, 1)
            y_test = np.array(y_test).reshape(-1, 1)

            train_arr = np.c_[X_train_transformed, y_train]
            test_arr = np.c_[X_test_transformed, y_test]

            # ============================
            # SAVE
            # ============================
            save_numpy_array_data(
                self.data_transformation_config.transformed_train_file_path,
                train_arr
            )

            save_numpy_array_data(
                self.data_transformation_config.transformed_test_file_path,
                test_arr
            )

            save_object(
                self.data_transformation_config.transformed_object_file_path,
                preprocessor
            )

            logging.info("Data Transformation completed successfully")

            return DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )

        except Exception as e:
            raise Krishmitra(e, sys)