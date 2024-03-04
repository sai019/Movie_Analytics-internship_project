import os
import shutil
import sys
from io import BytesIO
from zipfile import ZipFile

import requests

from src.exception.exception import CustomException
from src.logging.logger import logging


def create_directories(*directories):
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def setup_directories(current_directory):
    local_directory = change_directory(current_directory, 2)
    data_directory = os.path.join(local_directory, "Data")
    raw_directory = os.path.join(data_directory, "raw")
    transformed_directory = os.path.join(data_directory, "transformed")
    try:
        create_directories(data_directory, raw_directory, transformed_directory)
    except Exception as e:
        raise CustomException(e, sys)
    return data_directory, raw_directory


def change_directory(current_directory, levels):
    new_directory = current_directory
    for _ in range(levels):
        new_directory = os.path.abspath(os.path.join(new_directory, ".."))
    return new_directory


def download_unzip_dataset(url, data_directory):
    response = requests.get(url)
    if response.status_code == 200:
        with ZipFile(BytesIO(response.content)) as zip_file:
            zip_file.extractall(data_directory)
            logging.info("Download and extraction successful.")
    else:
        logging.info(f"Failed to download. Status code: {response.status_code}")


def move_files(source_path, target_path):
    for item in os.listdir(source_path):
        source_item_path = os.path.join(source_path, item)
        target_item_path = os.path.join(target_path, item)
        shutil.move(source_item_path, target_item_path)
