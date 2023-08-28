from Product_Recommendation_System.components.data_ingestion import DataIngestionConfig, DataIngestion

class TrainingPipeline:
    def __init__(self):
         self.data_ingestion = DataIngestion()
    
    def start_training_pipeline(self):
         self.data_ingestion.initiate_data_ingestion()