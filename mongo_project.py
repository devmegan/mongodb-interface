import pymongo
import os
""" get env.py file for keys/URIs"""
from os import path
if path.exists("env.py"):
  import env 
  print("env.py imported")

MONGO_URI = os.environ.get('MONGO_URI') #get mongo URI from env.py
DB_NAME = "myTestDB" # database name
COLL_NAME = "myFirstMDB" # collection name

def mongo_connect(url):
    """ connect to my mongodb """
    try:
        # if connection successful, let user know
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        # if connection fails, let user know
        print ("Could not connect to Mongo %s") % e #interpolates error message into string. 
