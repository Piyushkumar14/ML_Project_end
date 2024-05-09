from src.MLProject import logger
from src.MLProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.MLProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.MLProject.pipeline.stage_03_data_transformation import DataTranformationTrainingPipeline

# logger.info("Welcome to our custom log")
STAGE_NAME   = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME   = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME   = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTranformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e