from src.DataScienceProject.logger import logging
from src.DataScienceProject.exception import CustomException,sys
from src.DataScienceProject.components.data_ingestion import DataIngestion
from src.DataScienceProject.components.data_ingestion import DataIngestionConfig

if __name__ =="__main__":   
  logging.info("The execution has started")
  
  
  try:
    data_ingestion=DataIngestion()
    data_ingestion.initiate_data_ingestion()
  except Exception as e:
    logging.info('Custom Exception')
    raise CustomException(e,sys)