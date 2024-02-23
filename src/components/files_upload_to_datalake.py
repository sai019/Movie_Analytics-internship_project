import os
import sys

from azure.storage.filedatalake import DataLakeServiceClient

from src.config.config import (
    CONNECTION_STRING,
    DIRECTORY_NAMES,
    FILE_SYSTEM_NAME,
    LOCAL_RAW_DIRECTORY,
    RAW_DATA
)
from src.exception.exception import CustomException
from src.logging.logger import logging
from src.utils.Data_Lake_utils import (
    create_directory,
    create_file_system,
    get_directory_client,
    get_file_system_client,
    list_directory_contents,
    upload_file_to_directory,
)


def get_datalake_client(connection_string):
    return DataLakeServiceClient.from_connection_string(connection_string)


def upload_files_to_datalake(connection_string, local_directory, file_system_name, directory_names):
    try:
        datalake_client = get_datalake_client(connection_string)
        file_system_client = get_or_create_file_system_clients(datalake_client, file_system_name)
        directory_clients = {}
        for directory_name in directory_names:
            directory_clients[directory_name] = get_or_create_directory_clients(file_system_client, directory_name)
        for key, value in directory_clients.items():
            if key == RAW_DATA:
                # Retrieve the value corresponding to the key "raw"
                directory_client = value
                logging.info(f"Uploading to Azure Data Lake Storage:{key}")
                upload_file_to_directory(directory_client, local_directory)
            else:
                pass
    except Exception as e:
        raise CustomException(e, sys)


def list_of_files(connection_string, file_system_name, directory_names):
    datalake_client = get_datalake_client(connection_string)
    file_system_client = get_or_create_file_system_clients(datalake_client, file_system_name)
    for directory_name in directory_names:
        if directory_name == RAW_DATA:
            paths = list_directory_contents(file_system_client, directory_name)
            if paths:
                logging.info(f"Directory contents in container - '{file_system_name}':")
                for path in paths:
                    logging.info(path)
            else:
                logging.info("No files found in the directory.")


def get_or_create_file_system_clients(datalake_client, file_system_name):
    file_systems = datalake_client.list_file_systems()
    containers = [fs.name for fs in file_systems]
    if file_system_name not in containers:
        return create_file_system(datalake_client, file_system_name)
    else:
        return get_file_system_client(datalake_client, file_system_name)


def get_or_create_directory_clients(file_system_client, directory_name):
    existing_directories = [dir_.name for dir_ in file_system_client.get_paths() if dir_.is_directory]
    if directory_name not in existing_directories:
        return create_directory(file_system_client, directory_name)
    else:
        return get_directory_client(file_system_client, directory_name)


def main():
    connection_string = CONNECTION_STRING
    file_system_name = FILE_SYSTEM_NAME
    directory_names = DIRECTORY_NAMES
    logging.info(directory_names)
    raw_directory = LOCAL_RAW_DIRECTORY
    logging.info(raw_directory)
    contents = os.listdir(raw_directory)
    logging.info("List of folders and files in the target directory:")
    for item in contents:
        logging.info(item)

    upload_files_to_datalake(connection_string, raw_directory, file_system_name, directory_names)
    list_of_files(connection_string, file_system_name, directory_names)


if __name__ == "__main__":
    main()
