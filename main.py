from src.MLProject import logger
from src.MLProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.MLProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.MLProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.MLProject.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from src.MLProject.pipeline.stage_05_model_evaluation import ModelEvaluatingPipeline

# logger.info("Welcome to our custom log")
STAGE_NAME   = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME   = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelEvaluatingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx=================x")
except Exception as e:
        logger.exception(e)
        raise e