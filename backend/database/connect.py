from pymongo import MongoClient, IndexModel, ASCENDING
from os import getenv

class Connection:

    client: MongoClient = None
    o_db_name = "scratch-db"
    database = "scratch-db"

    # Initializes MongoDb client (from env), and sets static variable to client
    @staticmethod
    def init() -> bool:
        if Connection.is_initialized(): return True
        ATLAS_URL = getenv("ATLAS_URL", "")
        if ATLAS_URL == "":
            print ("No ATLAS URL specified!")
            return False
        try:
            Connection.client = MongoClient(ATLAS_URL)
            Connection.database = f"{Connection.o_db_name}-{getenv('ENV', 'prod')}"
            # TODO: add other collections and indexes
            # Connection.client[Connection.database]["users"].create_indexes([
            #     IndexModel([
            #         ("username", ASCENDING),
            #         ("email", ASCENDING)
            #     ], unique=True)
            # ])
            return True
        except Exception as e:
            print (e)
            return False

    @staticmethod
    def is_initialized() -> bool:
        return Connection.client is not None

    @staticmethod
    def set_testing():
        Connection.database = f"{Connection.o_db_name}-test"
