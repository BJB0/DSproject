from src.DataScienceProject.logger import logging
from src.DataScienceProject.exception import CustomException,sys
from src.DataScienceProject.components.data_ingestion import DataIngestion
from src.DataScienceProject.components.data_ingestion import DataIngestionConfig
from src.DataScienceProject.components.data_transformation import DataTransformationConfig, DataTransformation

if __name__ =="__main__":   
  logging.info("The execution has started")
  
  
  
  try:
    data_ingestion=DataIngestion()
    train_data_path, test_data_path=data_ingestion.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    
  except Exception as e:
    logging.info('Custom Exception')
    raise CustomException(e,sys)