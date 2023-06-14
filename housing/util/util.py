import yaml
import sys, os
from housing.exception import HousingException
import numpy as np
import dill
import numpy as np
import pandas as pd
from housing.constant import *


# Helper functions in util.py
def read_yaml_file(file_path:str)->dict:
    """
    Reads a yaml file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path,'rb') as file_yaml:
            return yaml.safe_load( file_yaml)
    except Exception as e:
        raise HousingException(e,sys) from e


def save_numpy_array_data(file_path: str, array: np.array):
    """
    save numpy array data to file.
    file_path: str location of file to save.
    array: np.array data to save.
    """
    try: 
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
        

    except Exception as e:
        raise HousingException(e, sys) from e


def load_numpy_array_data(file_path: str)-> np.array:
    """
    load numpy array data from file
    file_path: str location of file to load.
    return: np.array data loaded
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)

    except Exception as e:
        raise HousingException(e,sys) from e


def save_object(file_path: str, obj):
    """
    file_path: str
    obj: object to be loaded
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise HousingException(e,sys) from e  


def load_obj(file_path: str):
    """
    file_path: str
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise HousingException(e,sys) from e


def load_data(file_path: str, schema_file_path: str)-> pd.DataFrame:
    try:
        dataset_schema = read_yaml_file(schema_file_path)
        schema = dataset_schema[DATASET_SCHEMA_COLUMNS_KEY]
        dataframe = pd.read_csv(file_path)
        error_message = ""

        for column in dataframe.columns:
            if column in list(schema.keys()):
                dataframe[column].astype(schema[column])
            else:
                error_message = f"{error_message} \n column: [{column}] is not in the schema."

        if len(error_message)>0:
            raise Exception(error_message)

    except Exception as e:
        raise HousingException(e,sys) from e