import yaml
import os,sys
from Backend.exception.exception import Krishmitra
from Backend.logger.logger import logging
import numpy as np
import dill
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score


def read_yaml_file(file_path:str)->dict:
    """
    Docstring for read_yaml_file
    
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: dict
    read the yaml file and return the contents as dictionary
    """
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise Krishmitra(e,sys) from e

def write_yaml_file(file_path:str,content:object,replace=False)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w") as yaml_file:
            yaml.dump(content,yaml_file)
    except Exception as e:
        raise Krishmitra(e,sys)

def save_numpy_array_data(file_path:str,array:np.array):
    """
    save numpy array to data file
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            np.save(file_obj,array)
    except Exception as e:
        raise Krishmitra(e,sys)
    
# to picke the object
def save_object(file_path:str,obj:object) -> None:
    """
    file_path: str location of the file to save
    obj: object to save
    return None
    """
    try:
        logging.info("enter into the save_object method of utils module to pickle the object")
        
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
        logging.info("exit from the save_object method of utils module after pickling the object")
    except Exception as e:
        raise Krishmitra(e,sys)
    
def load_object(file_path: str, ) -> object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} is not exists")
        with open(file_path, "rb") as file_obj:
            print(file_obj)
            return pickle.load(file_obj)
    except Exception as e:
        raise Krishmitra(e, sys) from e
    
def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    file_path: str location of file to load
    return: np.array data loaded
    """
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise Krishmitra(e, sys) from e
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise Krishmitra(e, sys)