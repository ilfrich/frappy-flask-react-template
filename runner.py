from application.config import AppConfig
from application.registry import AppRegistry
from flask import Flask
from pbu import Logger
import application.api.static_api as static_api
# API endpoint modules
from frappyflaskauth import register_endpoints as register_user_endpoints
# storage modules
from frappymongouser import UserStore, UserTokenStore

if __name__ == "__main__":
    config = AppConfig()
    logger = Logger("MAIN", log_folder=config.get_log_folder())
    logger.info("==========================================")
    logger.info("           Starting application")
    logger.info("==========================================")

    # ---- database and stores ----

    # fetch mongo config
    mongo_url, mongo_db = config.get_mongo_config()

    # initialise stores
    stores = {
        "user": UserStore(mongo_url=mongo_url, mongo_db=mongo_db, collection_name="users"),
        "user_tokens": UserTokenStore(mongo_url=mongo_url, mongo_db=mongo_db, collection_name="userTokens"),
    }

    UserStore(mongo_url=mongo_url, mongo_db=mongo_db, collection_name="users").initial_local_user_check("admin", "admin")

    # app registry holding config and stores
    registry = AppRegistry(config, stores)

    # create flask app
    app = Flask(__name__)
    # register endpoints
    static_api.register_endpoints(app, registry)
    # register endpoints for authentication and user management
    register_user_endpoints(app, stores["user"], stores["user_tokens"])

    # start flask app
    app.run(host=config.get_host_name(), port=config.get_port(), debug=config.is_debug())
