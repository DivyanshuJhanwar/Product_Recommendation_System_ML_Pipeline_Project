from Product_Recommendation_System.exception import CustomException
from Product_Recommendation_System.logger import logging
from Product_Recommendation_System.config.configuration import AppConfiguration
from Product_Recommendation_System.components.data_ingestion import DataIngestion
import os
from Product_Recommendation_System.pipeline.pipeline import TrainingPipeline
from Product_Recommendation_System.components.data_validation import DataValidation

def main():
    try:
        pipeline = TrainingPipeline()
        pipeline.start_training_pipeline()

    except Exception as e:
            logging.error(f"{e}")
            print(e)


if __name__ == "__main__":
     main()