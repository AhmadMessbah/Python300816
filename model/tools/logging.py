import os

import logging
import sys

class Logger:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("d:/logging.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )
    @classmethod
    def info(cls, message):
        logging.info(message)


    @classmethod
    def error(cls, message):
        logging.error(message)

