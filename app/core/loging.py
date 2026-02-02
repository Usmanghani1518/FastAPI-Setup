import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import sys


def setup_logger():
    """Setup logger with 10MB file rotation"""
    
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
   
    logger = logging.getLogger("brandmize")
    logger.setLevel(logging.INFO)
    
    
    logger.handlers.clear()
    
  
    console_handler = logging.StreamHandler(sys.stdout)
    console_formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    file_handler = RotatingFileHandler(
        filename=log_dir / "app.log",     
        maxBytes=10_000_000,               
        backupCount=5,                     
        encoding="utf-8"
    )
    
    file_formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    
    logger.propagate = False
    
    return logger


logger = setup_logger()