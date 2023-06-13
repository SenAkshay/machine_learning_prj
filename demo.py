from housing.pipeline.pipeline import Pipeline
from housing.logger import logging
from housing.config.configuration import Configuartion
from housing.component.data_transformation import DataTransformation

def main():
    try:
        # pipeline = Pipeline
        # pipeline.run_pipeline()
        # data_validation_config = Configuartion().get_data_transformation_config()
        # print(data_validation_config)
        schema_file_path = r"C:\Users\akssen\Downloads\Akshay_ML\A_Project_ML\machine_learning_prj\config\schema.yaml"
        file_path= r"C:\Users\akssen\Downloads\Akshay_ML\A_Project_ML\machine_learning_prj\housing.csv"

        df =DataTransformation.load_data(file_path = file_path, schema_file_path = schema_file_path)
        print(df.columns)
        print(df.dtypes)

    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=='__main__':
    main()
