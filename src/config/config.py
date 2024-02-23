import os

from dotenv import load_dotenv

from src.utils.file_utils import setup_directories

load_dotenv(override=True)  # Load environment variables from .env file

# Source Link
DATASET_URL = os.getenv("dataset_url")


# Azure Conf
DATASET_URL = os.getenv("dataset_url")
CONNECTION_STRING = os.getenv("connection_string")
FILE_SYSTEM_NAME = os.getenv("file_system_name")
DIRECTORY_NAMES = [os.getenv("directory_names_r"), os.getenv("directory_names_t")]
RAW_DATA = os.getenv("directory_names_r")

# Local directories Conf
current_directory = os.path.abspath(os.path.dirname(__file__))
LOCAL_DATA_DIRECTORY, LOCAL_RAW_DIRECTORY = setup_directories(current_directory)
