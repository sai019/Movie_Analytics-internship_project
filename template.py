import logging
import os
import sys
from pathlib import Path

FORMAT = "[%(asctime)s] %(levelname)s: %(message)s"

logging.basicConfig(
    level=logging.INFO,
    format=FORMAT,
    datefmt="%d/%m/%Y - %I:%M:%S %p",
    handlers=[logging.StreamHandler(sys.stdout)],
)

list_of_files = [
    "src/__init__.py",
    "src/components/__init__.py",
    "src/utils/__init__.py",
    "src/config/__init__.py",
    "src/logger/__init__.py",
    "src/exception/__init__.py",
    "src/pipeline/__init__.py",
    "Images/.gitkeep",
    "requirements.txt",
    "research/.gitkeep",
    "Docs/.gitkeep",
    "Data/raw/.gitkeep",
    "Data/transformed/.gitkeep",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating the dirctory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
