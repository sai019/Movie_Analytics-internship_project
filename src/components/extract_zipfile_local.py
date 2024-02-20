import os
import sys

from src.exception import CustomException
from src.logger import logging
from src.utils.file_utils import (
    create_directories,
    download_dataset,
    move_files,
    move_up_directory,
    unzip_dataset,
)


def setup_directories(current_directory):
    local_directory = move_up_directory(current_directory, 3)
    data_directory = os.path.join(local_directory, "Data")
    raw_directory = os.path.join(data_directory, "raw")
    transformed_directory = os.path.join(data_directory, "transformed")
    try:
        create_directories(data_directory, raw_directory, transformed_directory)
    except Exception as e:
        raise CustomException(e, sys)
    return data_directory, raw_directory


def check_if_files_exist(local_zip_file):
    return os.path.exists(local_zip_file)


def download_unzip_move_dataset(dataset_url, data_directory, raw_directory):
    local_zip_file = os.path.join(data_directory, "ml-1m.zip")
    if not check_if_files_exist(local_zip_file):
        try:
            logging.info("Downloading Dataset from the source link...")
            download_dataset(dataset_url, local_zip_file)
            logging.info("Extracting Folders/Files from the Zip file")
            unzip_dataset(local_zip_file, data_directory)
            logging.info("Moving files to 'Data/Raw' folder path")
            unzipped_folder = os.path.join(
                data_directory, os.listdir(data_directory)[0]
            )
            move_files(unzipped_folder, raw_directory)
            os.rmdir(unzipped_folder)
        except Exception as e:
            raise CustomException(e, sys)
    else:
        logging.info("Files already downloaded...")


def main():
    dataset_url = "https://files.grouplens.org/datasets/movielens/ml-1m.zip"
    current_directory = os.path.abspath(os.path.dirname(__file__))
    data_directory, raw_directory = setup_directories(current_directory)
    download_unzip_move_dataset(dataset_url, data_directory, raw_directory)
    contents = os.listdir(raw_directory)
    logging.info(f"List of folders and files in the target directory: {raw_directory}")
    for item in contents:
        logging.info(item)


if __name__ == "__main__":
    main()
