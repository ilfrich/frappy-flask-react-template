from typing import Dict
from pbumongo import AbstractMongoStore
from application.config import AppConfig


class AppRegistry:
    def __init__(self, config: AppConfig, stores: Dict[str, AbstractMongoStore]):
        self.config = config
        self.stores = stores

    def get_user_store(self):
        return self.stores["user"]
