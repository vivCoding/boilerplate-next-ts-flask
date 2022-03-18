import os
from pymongo import MongoClient

class Config(object):
    SESSION_TYPE = 'mongodb'
    SESSION_MONGODB = MongoClient(os.getenv("ATLAS_URL"))
    SESSION_SECRET_KEY = os.getenv("SESSION_SECRET")
    SESSION_COOKIE_SECURE = os.getenv("ENV", "dev") == "prod"
    SESSION_COOKIE_SAMESITE = 'None' if os.getenv("ENV", "dev") == "prod" else 'Lax'