from CNN_CLASSIFIER import logger
from CNN_CLASSIFIER.config.configuration import ConfigurationManager
from CNN_CLASSIFIER.components.model_evaluation import Evaluation

STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed successfully <<<<<< \n\n--------------------------------")
    except Exception as e:
        logger.exception(e)
        raise e