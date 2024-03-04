import os
import sys

from src.config.config import DATASET_URL, LOCAL_DATA_DIRECTORY, LOCAL_RAW_DIRECTORY
from src.exception.exception import CustomException
from src.logging.logger import logging
from src.utils.file_utils import download_unzip_dataset, move_files


def list_of_files(raw_directory):
    contents = os.listdir(raw_directory)
    for item in contents:
        logging.info(item)


def download_unzip_move_dataset(dataset_url, data_directory, raw_directory):
    contents = os.listdir(raw_directory)
    if not contents:
        try:
            logging.info("Downloading Dataset from the source link to Data folder")
            download_unzip_dataset(dataset_url, data_directory)
            logging.info("Moving files to 'Data/raw' folder path")
            unzipped_folder = os.path.join(
                data_directory, os.listdir(data_directory)[0]
            )
            move_files(unzipped_folder, raw_directory)
            logging.info(
                f"List of folders and files in the target directory: {raw_directory}"
            )
            list_of_files(raw_directory)
            os.rmdir(unzipped_folder)
        except Exception as e:
            raise CustomException(e, sys)
    else:
        logging.info(f"Files already downloaded to => {raw_directory}")
        list_of_files(raw_directory)


def main():
    dataset_url = DATASET_URL
    data_directory = LOCAL_DATA_DIRECTORY
    raw_directory = LOCAL_RAW_DIRECTORY
    download_unzip_move_dataset(dataset_url, data_directory, raw_directory)


if __name__ == "__main__":
    main()
