from typing import Tuple
from pbu import BasicConfig


DEFAULTS = {
    "HOSTNAME": "0.0.0.0",
    "PORT": 5333,
    "IS_DEBUG": "0",

    "DATA_FOLDER": "_data",
    "LOG_FOLDER": "_logs",

    "MONGO_URL": "mongodb://localhost:27017",
    "MONGO_DB": "mydatabase",
}

class AppConfig(BasicConfig):
    def __init__(self):
        super().__init__(DEFAULTS, ["DATA_FOLDER", "LOG_FOLDER"])

    def get_host_name(self) -> str:
        return self.get_config_value("HOSTNAME")

    def get_port(self) -> int:
        return int(self.get_config_value("PORT"))
    
    def is_debug(self) -> bool:
        return self.get_config_value("IS_DEBUG", "0") == "1"

    def get_log_folder(self) -> str:
        return self.get_config_value("LOG_FOLDER")

    def get_data_folder(self) -> str:
        return self.get_config_value("DATA_FOLDER")

    def get_mongo_config(self) -> Tuple[str, str]:
        return self.get_config_value("MONGO_URL"), self.get_config_value("MONGO_DB")
