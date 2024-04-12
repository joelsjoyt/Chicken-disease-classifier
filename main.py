from CNN_CLASSIFIER import logger
from CNN_CLASSIFIER.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNN_CLASSIFIER.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CNN_CLASSIFIER.pipeline.stage_03_model_training import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed successfully <<<<<< \n\n--------------------------------")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f">>>>>>***------------***----------------***")
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed successfully <<<<<< \n\n--------------------------------")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "Model Training"
try:
    logger.info(f">>>>>>***------------***----------------***")
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed successfully <<<<<< \n\n--------------------------------")
except Exception as e:
    logger.exception(e)
    raise e 
