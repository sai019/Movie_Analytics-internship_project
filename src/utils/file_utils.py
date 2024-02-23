import os
import shutil
import sys
import zipfile

import requests

from src.exception.exception import CustomException


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


def download_dataset(url, local_zip_file):
    response = requests.get(url)
    with open(local_zip_file, "wb") as f:
        f.write(response.content)


def unzip_dataset(zip_file, extract_path):
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(extract_path)


def move_files(source_path, target_path):
    for item in os.listdir(source_path):
        source_item_path = os.path.join(source_path, item)
        target_item_path = os.path.join(target_path, item)
        shutil.move(source_item_path, target_item_path)
