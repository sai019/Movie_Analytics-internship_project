import os
import sys
import logging
from pathlib import Path

# FORMAT(Custom) can be edited according to your preference

# logs can be saved in a file using filename='logs.log' in logging.basicConfig()

FORMAT = '[%(asctime)s] %(levelname)s: %(message)s'

logging.basicConfig(level=logging.INFO, format=FORMAT,datefmt= '%d/%m/%Y - %I:%M:%S %p',
                    handlers=[logging.StreamHandler(sys.stdout)])

# list of files should be according to your project structure

project_name = "Movie_Analytics"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "Images/.gitkeep",
    "requirements.txt",
    "research/.gitkeep",
    "Docs/.gitkeep",
    "Data/raw/.gitkeep",
    "Data/transformed/.gitkeep"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating the dirctory: {filedir} for the file: {filename}")

    else:
        logging.info(f"{filedir} is already exists")    

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")        