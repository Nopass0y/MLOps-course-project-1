import os
import pandas as pd
from src.logger import get_logger
from src.customer_exception import CustomerException
import yaml

logger = get_logger(__name__)

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path) :
            raise FileNotFoundError(f"File is not in the given path")
        
        with open(file_path, "r") as ymal_file :
            config = yaml.safe_load(ymal_file)
            logger.info("Successfully read the YAML file")
            return config
    except Exception as e :
        logger.error("Error while reading YAML file")
        raise CustomerException("Failed to read YAML file")

def load_data(path):
    try:
        logger.info("Loading data")
        return pd.read_csv(path)
    except Exception as e:
        logger.error(f"Error loading the data {e}")
        raise CustomerException("Failed to load data" , e)
