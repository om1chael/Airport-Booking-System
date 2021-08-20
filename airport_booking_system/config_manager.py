import configparser
import os
from definitions import ROOT_DIR

_config = configparser.ConfigParser()
_config.read(os.path.join(ROOT_DIR, "config.ini"))

BASE_URL = _config['default']['base_url']

if __name__ == "__main__":
    print("This is the config_manager file")
