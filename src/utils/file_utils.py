import os
import shutil
import zipfile

import requests


def create_directories(*directories):
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


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


def move_up_directory(current_directory, levels):
    """
    Move up in the directory structure by the specified number of levels.
    Args:
    - current_directory (str): The current directory.
    - levels (int): The number of levels to move up.

    Returns:
    - str: The path of the new directory after moving up.
    """
    new_directory = current_directory
    for _ in range(levels):
        new_directory = os.path.abspath(os.path.join(new_directory, ".."))
    return new_directory
