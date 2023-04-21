import yaml
import sys
from housing.exception import HousingException

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