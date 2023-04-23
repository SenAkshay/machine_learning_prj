from housing.config.configuration import Configuartion
from housing.logger import logging
from housing.exception import HousingException
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import DataValidationConfig
from housing.constant import *
import os,sys

class DataValidation:

    def __init__(self, 
                data_validation_config: DataValidationConfig,
                data_ingestion_artifact: DataIngestionArtifact
                ):
        try:
            logging.info("Initiating Data Validation")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e


    def is_train_test_file_exists(self)->bool:
        try:
            logging.info("Checking presence of train and test data files")
            is_train_file_exists = False
            is_test_file_exists = False

            train_file_path=self.data_ingestion_artifact.train_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path

            is_train_file_exists = os.path.exists(train_file_path)
            is_test_file_exists = os.path.exists(test_file_path)

            logging.info("Finished checking train and test file presence")

            is_available = train_file_path & test_file_path
            if not is_available:
                message = f"Training file: {train_file_path} or testing file: {test_file_path}"\
                    " is missing"
                logging.info(message)
                raise Exception(message)

            return is_train_file_exists & is_test_file_exists
        except Exception as e:
            raise HousingException(e,sys) from e


    def validate_dataset_schema(self)-> bool:
        try:
            logging.info("Initiating dataset schema validation")
            validation_status = False

            # validate training and testing dataset using schema file
            # 1. no. of columns
            # 2. check the value of ocean proximity
            # 3. check column names
            # 4. acceptable values

            return validation_status
        except Exception as e:
            raise HousingException(e,sys) from e


    def Initiate_data_validation(self):
        try:
            logging.info("Initiating data validation")
            self.is_train_test_file_exists()

        except Exception as e:
            raise HousingException(e,sys) from e