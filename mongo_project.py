import pymongo
import os
""" get env.py file for keys/URIs"""
from os import path
if path.exists("env.py"):
    import env
    print("env.py imported")

MONGO_URI = os.environ.get('MONGO_URI')  # get mongo URI from env.py
DB_NAME = "myTestDB"  # database name
COLL_NAME = "myFirstMDB"  # collection name


def mongo_connect(url):
    """ connect to my mongodb """
    try:
        # if connection successful, let user know
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        # if connection fails, let user know
        print("Could not connect to Mongo %s") % e  # interpolates error message into string.


def show_menu():
    """display menu options to user"""
    print("")
    print("1: Add a Record")
    print("2: Find a Record")
    print("3: Edit a Record")
    print("4: Delete a Record")
    print("5: Exit")

    option = input("Enter Option: ")
    return option


def main_loop():
    """ call menu every time we come back to it """
    while True:  # will basically run forever...
        option = show_menu()  # store result of show_menu function in variable option
        if option == "1":
            print("You have selected option 1")
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            print("Connection will now close")
            conn.close()
            break
        else:
            print("Invalid Option")
            print("")


conn = mongo_connect(MONGO_URI)  # call function to connect to mongodb

coll = conn[DB_NAME][COLL_NAME]  # set connection
print("\n"*3 + str(coll) + "\n"*3)


main_loop()  # call main loop to continue displaying options/processing user input
