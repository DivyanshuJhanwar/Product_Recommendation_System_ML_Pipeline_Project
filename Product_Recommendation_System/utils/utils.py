import os, sys, yaml

from Product_Recommendation_System.exception import CustomException
from Product_Recommendation_System.logger import logging

def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        logging.error(e)
        raise CustomException(e)