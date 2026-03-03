import os,sys
from urllib.parse import urlparse
from Backend.exception.exception import Krishmitra
from Backend.logger.logger import logging
from Backend.crop_yield.entity.artifacts_entity import DataTransformationArtifact,ModelTrainerArtifact
from Backend.crop_yield.entity.config_entity import ModelTrainerConfig
from Backend.crop_yield.utils.main_utils import save_object,save_numpy_array_data,load_numpy_array_data,load_object,evaluate_models
from Backend.crop_yield.utils.ml_utils.metric.acuuracy import get_score
from Backend.crop_yield.utils.ml_utils.model.estimator import KrishmitraModel
import mlflow


#algortithms
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    AdaBoostRegressor
)
import dagshub
os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/navadeepgoud12/krishmitra.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="navadeepgoud12"
os.environ["MLFLOW_TRACKING_PASSWORD"]="02ebde13bf67930a47194beb38fc1a3a52c8c659"
try:
    dagshub.init(repo_owner='navadeepgoud12', repo_name='krishmitra', mlflow=True)
except Exception as e:
    logging.warning(f"DagHub initialization failed: {e}")

import mlflow
import mlflow.sklearn
from urllib.parse import urlparse

class ModelTrainer:
    def __init__(self,model_trainer_config:ModelTrainerConfig,data_transformation_artifact:DataTransformationArtifact):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise Krishmitra(e,sys)


    def track_mlflow(self, best_model, metrics):
        try:
            mlflow.set_registry_uri("https://dagshub.com/navadeepgoud12/krishmitra.mlflow")
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

            with mlflow.start_run():

                #  Extract values from your AccuracyArtifact
                mse = metrics.mean_squared_error
                mae = metrics.mean_absolute_error
                r2 = metrics.r2_score

                #  Log metrics
                mlflow.log_metric("MSE", mse)
                mlflow.log_metric("MAE", mae)
                mlflow.log_metric("R2 Score", r2)

                # ✅ Log model
                mlflow.sklearn.log_model(best_model, "model")
                

                # ✅ Register model (if not local file system)
                if tracking_url_type_store != "file":
                    mlflow.sklearn.log_model(
                        best_model,
                        "model",
                        registered_model_name="crop_yield_model"
                    )
                else:
                    mlflow.sklearn.log_model(best_model, "model")

        except Exception as e:
            raise e
        
    def train_model(self,X_train,y_train,X_test,y_test):
        models = {
                "Random Forest": RandomForestRegressor(verbose=1),
                #"Decision Tree": DecisionTreeRegressor(),
                #"Gradient Boosting": GradientBoostingRegressor(verbose=1),
                #"XGboost": XGBRegressor(verbosity=1),
                #"AdaBoost": AdaBoostRegressor(),
            }
        params = {
    #"Decision Tree": {
        #'criterion': ['squared_error', 'friedman_mse', 'absolute_error'],
        #'max_depth': [3, 5, 10, None],
        #'min_samples_split': [2, 5, 10]
    #},

    "Random Forest": {
        'n_estimators': [8, 16, 32, 64, 128],
        'max_depth': [3, 5, 10, None]
    },

    #"Gradient Boosting": {
        #'learning_rate': [0.1, 0.01, 0.05],
        #'subsample': [0.6, 0.7, 0.8, 0.9],
        #'n_estimators': [32, 64, 128],
        #'max_depth': [3, 5, 6]
   # },
    
    #"XGboost": {
        #'learning_rate': [0.1, 0.05, 0.01],
        #'n_estimators': [32, 64, 128],
        #'max_depth': [3, 5, 6],
        #'subsample': [0.7, 0.8, 0.9],
        #'colsample_bytree': [0.7, 0.8, 0.9]
    #},

    #"AdaBoost": {
        #'learning_rate': [0.1, 0.01, 0.001],
        #'n_estimators': [32, 64, 128]
    # }
    }
        
            
        
        model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                          models=models,param=params)
        ## To get best model score from dict
        best_model_score = max(sorted(model_report.values()))

        ## To get best model name from dict

        best_model_name = list(model_report.keys())[
            list(model_report.values()).index(best_model_score)
        ]
        best_model = models[best_model_name]
        y_train_pred=best_model.predict(X_train)

        accuracy_train_metric=get_score(y_true=y_train,y_pred=y_train_pred)
        
        ## Track the experiements with mlflow
        self.track_mlflow(best_model,accuracy_train_metric)


        y_test_pred=best_model.predict(X_test)
        accuracy_test_metric=get_score(y_true=y_test,y_pred=y_test_pred)

        self.track_mlflow(best_model,accuracy_test_metric)

        preprocessor = load_object(file_path=self.data_transformation_artifact.transformed_object_file_path)
            
        model_dir_path = os.path.dirname(self.model_trainer_config.trained_model_file_path)
        os.makedirs(model_dir_path,exist_ok=True)

        Krishmitra_Model=KrishmitraModel(preprocessor=preprocessor,model=best_model)
        save_object(self.model_trainer_config.trained_model_file_path,obj=Krishmitra_Model)
        #model pusher
        os.makedirs("final_model", exist_ok=True)
        save_object("final_model/model.pkl",Krishmitra_Model)
        

        ## Model Trainer Artifact
        model_trainer_artifact=ModelTrainerArtifact(trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                             train_metric_artifact=accuracy_train_metric,
                             test_metric_artifact=accuracy_test_metric
                             )
        logging.info(f"Model trainer artifact: {model_trainer_artifact}")
        
        return model_trainer_artifact
    
    
            
    def initate_model_trainer(self)->ModelTrainerArtifact:
        try:
            train_file_path = self.data_transformation_artifact.transformed_train_file_path
            test_file_path = self.data_transformation_artifact.transformed_test_file_path

            #loading training array and testing array
            train_arr = load_numpy_array_data(train_file_path)
            test_arr = load_numpy_array_data(test_file_path)

            x_train, y_train, x_test, y_test = (
                train_arr[:, :-1],
                train_arr[:, -1],
                test_arr[:, :-1],
                test_arr[:, -1],
            )

            model_trainer_artifact=self.train_model(x_train,y_train,x_test,y_test)
            return model_trainer_artifact
        except Exception as e:
            raise Krishmitra(e,sys)