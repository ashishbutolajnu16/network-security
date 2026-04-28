import sys

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import (
    DataIngestionConfig,
    TrainingPipelineconfig,
)
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

if __name__ == "__main__":
    try:
        trainingconfigpipeline = TrainingPipelineconfig()
        data_ingestion_config = DataIngestionConfig(trainingconfigpipeline)
        dataingestion = DataIngestion(data_ingestion_config)
        logging.info('Initate data ingestion')
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as e:
        raise NetworkSecurityException(e, sys)