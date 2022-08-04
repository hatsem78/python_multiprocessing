import os
import time
from enum import Enum
from logging.config import dictConfig

from dotenv import load_dotenv
from logging import Formatter, Logger, StreamHandler

# Extensions formats for Tesseract
from pydantic import BaseModel

allowed_ext = {'png', 'pdf', 'jpeg', 'jpg'}
# Extensions formats for Barcodes
allowed_ext_barcode_qr = {'tiff', 'tif'}
allowed_ext_barcode_pdf417 = {'png', 'jpeg', 'jpg'}

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


def get_logger(name):
    config = Config()

    if config.disable_3rd_party_logs:
        dictConfig({
            'version': 1,
            'disable_existing_loggers': True,
        })

    level = os.getenv("LOGGING_LEVEL", "DEBUG")
    message_format = "[%(asctime)s] [%(levelname)s] %(message)s"
    timestamp_format = "%Y-%m-%dT%H:%M:%SZ"

    formatter = Formatter(fmt=message_format, datefmt=timestamp_format)
    formatter.converter = time.gmtime

    handler = StreamHandler()
    handler.setFormatter(formatter)
    logger = Logger(name, level=level)
    logger.addHandler(handler)

    return logger


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_ext


def allowed_file_barqr(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_ext_barcode_qr


def allowed_file_bar417(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_ext_barcode_pdf417


class Config(object):
    MULTIMEDIA_TOPIC = "stg"
    API_TOPIC = ""
    __linux = ''
    __disable_3rd_party_logs = 'FALSE'
    __requests_timeout = 30
    ACTIVE_CONSUMER_ENV = ""
    ACTIVE_DIFF_CHECKER_ENV = ""

    def __init__(self):
        """
            Environment Variable system
        """
        self.linux = os.getenv('LINUX', 'True')
        self.url_ocr = os.getenv('URL_OCR', '')
        self.ssl_post = os.getenv('SSL_POST', 'False')
        self.disable_3rd_party_logs = os.getenv(
            'DISABLE_3RD_PARTY_LOGS', 'FALSE'
        )
        self.requests_timeout = os.getenv('REQUESTS_TIMEOUT', '30')
        self.ACTIVE_CONSUMER_ENV = os.getenv('ACTIVE_CONSUMER_ENV', 'stg')
        self.ACTIVE_DIFF_CHECKER_ENV = os.getenv('ACTIVE_DIFF_CHECKER_ENV', 'stg')

    @property
    def linux(self):
        return self.__linux

    @linux.setter
    def linux(self, value):
        if value is None:
            raise ValueError
        elif not isinstance(value, (str,)):
            raise TypeError("linux must be str")
        self.__linux = True if value == 'True' else False

    @property
    def ssl_post(self):
        return self.__ssl_post

    @ssl_post.setter
    def ssl_post(self, value):
        if value is None:
            raise ValueError
        elif not isinstance(value, (str,)):
            raise TypeError("ssl_post must be str")
        self.__ssl_post = True if value == 'True' else False

    @property
    def disable_3rd_party_logs(self):
        return self.__disable_3rd_party_logs

    @disable_3rd_party_logs.setter
    def disable_3rd_party_logs(self, value):
        if value is None:
            raise ValueError
        elif not isinstance(value, (str,)):
            raise TypeError("disable_3rd_party_logs must be str")
        self.__disable_3rd_party_logs = \
            True if value.lower() == 'true' else False

    @property
    def requests_timeout(self):
        return self.__requests_timeout

    @requests_timeout.setter
    def requests_timeout(self, value):
        if value is None:
            raise ValueError
        elif not isinstance(value, (str,)):
            raise TypeError("requests_timeout must be str")
        self.__requests_timeout = int(value)


class Task(str, Enum):
    TASK_1 = "TASK_1"
    TASK_2 = "TASK_2"
    TASK_3 = "TASK_3"
    TASK_4 = "TASK_4"



