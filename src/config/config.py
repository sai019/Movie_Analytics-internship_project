# Variables holding different sensitive data like Api keys and paths used in the project
import os

from dotenv import load_dotenv

load_dotenv()


def get_input_path():
    return os.environ.get("INPUT_DATA_PATH")


def get_output_path():
    return os.environ.get("OUTPUT_DATA_PATH")


def get_api_key():
    return os.environ.get("API_KEY")
