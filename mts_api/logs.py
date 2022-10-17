import imp
import logging
import os
import yaml
import sys
import time

from config.config import log_file, log_time


def echo_to_file(string):
    os.system(f"echo '{string}' >> {log_time}")

logging.getLogger('').handlers = []
logging.getLogger('app').setLevel(logging.DEBUG)
FORMAT = '%(asctime)s - %(funcName)s - %(levelname)s - %(message)s'
logging.basicConfig(filename=log_file, filemode='w', format=FORMAT)
logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)


def callback(status=None, info=None):
    if status == 1:
        return_yaml = {"Status": "OK", "Response": info}
        logger.info("\n" + yaml.dump(return_yaml, default_style=False, sort_keys=False))
    else:
        return_yaml = {"Status": "ERROR", "Message": info}
        logger.error("\n" + yaml.dump(return_yaml, default_style=False, sort_keys=False))
    return yaml.dump(return_yaml, default_style=False, sort_keys=False)
