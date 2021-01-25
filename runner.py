from flask import Flask
from pbu import Logger
from config import load_config, get_log_folder, is_debug, get_port
import api.static_api as static_api
# API endpoint modules
from frappyflaskauth import register_endpoints as register_user_endpoints, check_login_state
from frappyflaskdataset import register_endpoints as register_data_endpoints
from frappyflaskcontent import register_endpoints as register_content_endpoints
# storage modules
from frappymongouser import UserStore, UserTokenStore
from frappymongodataset import DataStore
from frappymongocontent import ContentStore

if __name__ == "__main__":
    logger = Logger("MAIN", log_folder=get_log_folder())
    logger.info("==========================================")
    logger.info("           Starting application")
    logger.info("==========================================")

    # load config from .env file
    config = load_config()

    # ---- database and stores ----

    # fetch mongo config
    from config import get_mongodb_config
    mongo_url, mongo_db = get_mongodb_config()

    # initialise stores
    stores = {
        "user": UserStore(mongo_url=mongo_url, mongo_db=mongo_db, collection_name="users"),
        "user_tokens": UserTokenStore(mongo_url=mongo_url, mongo_db=mongo_db, collection_name="userTokens"),
        "data": DataStore(mongo_url=mongo_url, mongo_db=mongo_db, collection_name="dataSets"),
        "content": ContentStore(mongo_url=mongo_url, mongo_db=mongo_db, collection_name="content"),
    }

    # create flask app
    app = Flask(__name__)
    # register endpoints
    static_api.register_endpoints(app)
    # register endpoints for authentication and user management
    register_user_endpoints(app, stores["user"], stores["user_tokens"])
    # register endpoints for data management and retrieval
    register_data_endpoints(app, stores["data"], {
        "manage_permission": "data",  # permission required to manage content
        "login_check_function": check_login_state,  # this function ties the authentication module into this one
    })
    # register endpoints for content management
    register_content_endpoints(app, stores["content"], {
        "manage_permission": "content",
        "login_check_function": check_login_state,
    })

    # start flask app
    app.run(host='0.0.0.0', port=get_port(), debug=is_debug())
