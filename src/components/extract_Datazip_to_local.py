import os
import sys

from src.config.config import DATASET_URL, LOCAL_DATA_DIRECTORY, LOCAL_RAW_DIRECTORY
from src.exception.exception import CustomException
from src.logging.logger import logging
from src.utils.file_utils import download_dataset, move_files, unzip_dataset

# def check_if_files_exist(local_zip_file):
#     return os.path.exists(local_zip_file)


def download_unzip_move_dataset(dataset_url, data_directory, raw_directory):
    local_zip_file = os.path.join(data_directory, "ml-1m.zip")
    if not os.path.exists(local_zip_file):
        try:
            logging.info("Downloading Dataset from the source link to Data folder")
            download_dataset(dataset_url, local_zip_file)
            logging.info("Extracting Folders/Files from the Zip file")
            unzip_dataset(local_zip_file, data_directory)
            logging.info("Moving files to 'Data/raw' folder path")
            unzipped_folder = os.path.join(data_directory, os.listdir(data_directory)[0])
            move_files(unzipped_folder, raw_directory)
            os.rmdir(unzipped_folder)
        except Exception as e:
            raise CustomException(e, sys)
    else:
        logging.info("Files already downloaded...")


def main():
    dataset_url = DATASET_URL
    # logging.info(dataset_url)
    data_directory = LOCAL_DATA_DIRECTORY
    # logging.info(data_directory)
    raw_directory = LOCAL_RAW_DIRECTORY
    logging.info(raw_directory)
    download_unzip_move_dataset(dataset_url, data_directory, raw_directory)
    contents = os.listdir(raw_directory)
    logging.info(f"List of folders and files in the target directory: {raw_directory}")
    for item in contents:
        logging.info(item)


if __name__ == "__main__":
    main()
