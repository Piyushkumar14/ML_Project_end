import os
from src.MLProject import  logger
from src.MLProject.entity.config_entity import DataValidationConfig
import pandas as pd

# %%
class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            # all_types = dict(data.info)

            all_schema = self.config.all_schema.keys()
            # all_schema_values = self.config.all_schema.values()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status {validation_status}")
            return validation_status
        except Exception as e:
            raise e
