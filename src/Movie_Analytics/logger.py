import os
import sys
import logging
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

log_dir = "logs"
log_filename = f"{datetime.now().strftime('%d_%m_%Y_')}.log"
log_filepath = os.path.join(log_dir, log_filename)
os.makedirs(log_dir, exist_ok=True)

FORMAT = '[%(asctime)s] %(levelname)s: %(message)s (Filename: [%(filename)s] -> Line: %(lineno)d)'

file_handler = TimedRotatingFileHandler(
    log_filepath,
    when="midnight",
    interval=1,
    #backupCount=7,  # Keep up to 7 days of logs
    encoding="utf-8"
)

file_handler.setFormatter(logging.Formatter(FORMAT))

logging.basicConfig(
        level=logging.INFO,
        format=FORMAT,
        datefmt='%d/%m/%Y - %I:%M:%S %p',
        handlers=[logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)]
    )