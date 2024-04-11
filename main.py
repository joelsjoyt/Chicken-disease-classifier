from CNN_CLASSIFIER import logger
from CNN_CLASSIFIER.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed successfully <<<<<< \n\n--------------------------------")
except Exception as e:
    logger.exception(e)
    raise e 
