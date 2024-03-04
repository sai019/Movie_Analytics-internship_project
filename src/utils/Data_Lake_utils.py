import os
import sys

from src.exception.exception import CustomException


def get_file_system_client(datalake_client, file_system_name):
    try:
        file_system_client = datalake_client.get_file_system_client(file_system=file_system_name)
    except Exception as e:
        raise CustomException(e, sys)
    return file_system_client


def create_file_system(datalake_client, file_system_name):
    try:
        file_system_client = datalake_client.create_file_system(file_system=file_system_name)
    except Exception as e:
        raise CustomException(e, sys)
    return file_system_client


def get_directory_client(file_system_client, directory_name):
    try:
        directory_client = file_system_client.get_directory_client(directory=directory_name)
    except Exception as e:
        raise CustomException(e, sys)
    return directory_client


def create_directory(file_system_client, directory_name):
    try:
        directory_client = file_system_client.create_directory(directory=directory_name)
    except Exception as e:
        raise CustomException(e, sys)
    return directory_client


def upload_file_to_directory(directory_client, local_directory):
    try:
        for item in os.listdir(local_directory):
            item_path = os.path.join(local_directory, item)
            if os.path.isfile(item_path):
                file_client = directory_client.get_file_client(item)
                exists = file_client.exists()
                if not exists and item.endswith(".dat"):
                    file_client = directory_client.get_file_client(item)
                    with open(item_path, "rb") as data:
                        file_client.upload_data(data, overwrite=True)
                else:
                    pass
    except Exception as e:
        raise CustomException(e, sys)


def list_directory_contents(file_system_client, directory_name):
    paths = []
    try:
        for path in file_system_client.get_paths(path=directory_name):
            paths.append(path.name)
        return paths
    except Exception as e:
        raise CustomException(e, sys)


def delete_directory(directory_client):
    try:
        directory_client.delete_directory()
    except Exception as e:
        raise CustomException(e, sys)
