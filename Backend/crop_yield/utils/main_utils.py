import yaml
import os,sys
from Backend.exception.exception import Krishmitra
from Backend.logger.logger import logging

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