from housing.config.configuration import Configuartion
from housing.logger import logging
from housing.exception import HousingException
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataValidationArtifact
from housing.constant import *
import os,sys
import pandas as pd
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab
import json


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

    def get_train_test_df(self):
        try:
            logging.info("Extracting data frames from train and test file")
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df, test_df
        except Exception as e:
            raise HousingException(e,sys) from e

    def validate_dataset_schema(self)-> bool:
        try:
            logging.info("Initiating dataset schema validation")
            validation_status = False
            self.get_train_test_df()
            # validate training and testing dataset using schema file
            # 1. no. of columns
            # 2. check the value of ocean proximity
            # 3. check column names
            # 4. acceptable values

            return validation_status
        except Exception as e:
            raise HousingException(e,sys) from e

    def get_and_save_data_drift_report(self):
        try:
            logging.info("Saving data drift report")

            train_df, test_df  = self.get_train_test_df()
            profile = Profile(sections=DataDriftProfileSection())
            profile.calculate(train_df, test_df)
            report = json.loads(profile.json()) # to dictionary or list instead of string.
            report_file_path = self.data_validation_config.report_file_path
            report_dir = os.path.dirname(report_file_path)

            with open(report_dir,"w") as report_file:
                json.dump(report, report_file, indent=6)
            return report
        except Exception as e:
            raise HousingException(e,sys) from e

    def save_data_drift_report_page(self):
        try:
            logging.info("Saving data drift report page")
            dashboard = Dashboard(tabs=[DataDriftTab()])
            train_df, test_df  = self.get_train_test_df()
            dashboard.calculate(train_df, test_df)
            report_page_file_path = self.data_validation_config.report_page_file_path
            report_page_dir  = os.path.dirname(report_page_file_path)
            os.makedirs(report_page_dir, exist_ok=True)

            dashboard.save(self.data_validation_config.report_file_path)

        except Exception as e:
            raise HousingException(e,sys) from e

    def is_data_drift_found(self):
        try:
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()
            return True
        except Exception as e:
            raise HousingException(e,sys) from e

    def initiate_data_validation(self)-> DataValidationArtifact:
        try:
            logging.info("Initiating data validation")
            self.is_train_test_file_exists()
            self.validate_dataset_schema()
            self.is_data_drift_found()

            data_validation_artifact = DataValidationArtifact(
                schema_file_path=self.data_validation_config.schema_file_path,
                report_file_path=self.data_validation_config.report_file_path,
                report_page_file_path=self.data_validation_config.report_page_file_path,
                is_validated=True,
                message="Data Validation performed successfully"
            )
            logging.info(f"Data Validation artifact: {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise HousingException(e,sys) from e