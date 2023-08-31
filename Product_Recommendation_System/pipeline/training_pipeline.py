from Product_Recommendation_System.components.data_ingestion import DataIngestion
from Product_Recommendation_System.components.data_validation import DataValidation
from Product_Recommendation_System.components.data_transformation import DataTransformation
from Product_Recommendation_System.components.model_training import ModelTrainer



class TrainingPipeline:
    def __init__(self):
         self.data_ingestion = DataIngestion()
         self.data_validation = DataValidation()
         self.data_transformation = DataTransformation()
         self.model_training = ModelTrainer()
    

    def start_training_pipeline(self):
        """
        Starts the training pipeline
        :return: none
        """
        self.data_ingestion.initiate_data_ingestion()
        self.data_validation.initiate_data_validation()
        self.data_transformation.initiate_data_transformation()
        self.model_training.initiate_model_trainer()