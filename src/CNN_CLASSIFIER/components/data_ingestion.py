import os
import zipfile
from pathlib import Path
import urllib.request as request
from CNN_CLASSIFIER import logger
from CNN_CLASSIFIER.utils.common import get_size
from CNN_CLASSIFIER.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        """
        This function downloads the dataset from the url specified 
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download complete! With following info:  \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
            
    def extract_zip_file(self):
        """
        This function extracts the zip file into data directory
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            