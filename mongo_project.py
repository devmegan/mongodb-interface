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
    print("MAIN MENU")
    print("1: Add a Record")
    print("2: Find a Record")
    print("3: Edit a Record")
    print("4: Delete a Record")
    print("5: Exit")

    option = input("Enter Option: ")
    return option


# CRUD FUNCTIONS
def get_record():
    "fetch and display record from db"
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    print("")
    print("Searching for a record of: {} {}".format(first, last))

    try:
        # find record that matches name
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("")
        print("Error fetching record")

    if not doc:  # if no record found, an empty doc var is returned
        print("")
        print("No records found matching {} {}.".format(first, last))

    return doc


def add_record():
    """ get input and create new record from it """
    print("")
    # get user input for record
    first = input("Enter First Name > ")
    last = input("Enter Last Name > ")
    dob = input("Enter Date of Birth (DD/MM/YYYY) > ")
    gender = input("Enter gender > ")
    hair_colour = input("Enter hair colour > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

    # construct string to feed to new record statement
    new_rec = {'first': first.lower(), 'last': last.lower(), 'dob': dob, 'gender': gender.lower(), 'hair_colour': hair_colour.lower(), 'occupation': occupation.lower(), 'nationality': nationality.lower()}

    try:
        # insert the new record into the db
        coll.insert_one(new_rec)
        print("")
        print("Record successfully created")
        print("New Record: " + str(new_rec))
    except:
        # generic error statement
        print("")
        print("Error writing to Mongo")

def find_record():
    """ display record if one found """
    doc = get_record()
    if doc:
        print("")
        for key, value in doc.items(): 
            if key != "_id":  # don't want to display id to user
                print(key.capitalize() + ": " + value.capitalize())

def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for key, value in doc.items():
            if key != "_id":
                update_doc[key] = input(key.capitalize() + " [" + value + "] > ")
                if update_doc[key] == "":
                    update_doc[key] = value
        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("Document updated")
            print("Updated Record: " + str(update_doc))
        except:
            print("Error accessing the database")






def delete_record():
    doc = get_record()
    if doc:
        print("")
        for key, value in doc.items():
            if key != "_id":
                print(key.capitalize() + ": " + value.capitalize())
        print("")
        confirmation = input("Is this the document you want to delete?\nY/N > ")
        print("")

        if confirmation.lower() == 'y':
            try:
                coll.delete_one(doc)
                print("Document deleted!")
            except:
                print("Error deleting the document")



def main_loop():
    """ call menu every time we come back to it """
    while True:  # will basically run forever...
        option = show_menu()  # store result of show_menu function in variable option
        if option == "1":
            print("You have selected option 1")
            add_record()
        elif option == "2":
            print("You have selected option 2")
            find_record()
        elif option == "3":
            print("You have selected option 3")
            edit_record()
        elif option == "4":
            print("You have selected option 4")
            delete_record()
        elif option == "5":
            print("Closing Connection to Mongo")
            conn.close()
            break
        else:
            print("Invalid Option")
            print("")


conn = mongo_connect(MONGO_URI)  # call function to connect to mongodb

coll = conn[DB_NAME][COLL_NAME]  # set connection
print("\n"*3 + str(coll) + "\n"*3)


main_loop()  # call main loop to continue displaying options/processing user input
