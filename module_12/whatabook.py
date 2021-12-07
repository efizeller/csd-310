import sys
import mysql.connector
from mysql.connector import errorcode

# configures the connection information the program will use to connect to the database.
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}
# function that shows the user menu when called. 
def show_menu():
    print("\n-- Main Menu --")
    print("1. View Books\n2. View Store Locations\n3. My Account\n4) Exit Program")

    # this try/except catches any user input errors that may occur such as entering letters instead of int, and then gives an error message related to what failed if a failure does occur.
    try:
        choice = int(input("Type in a number to choose a menu option: "))
        return choice

    except ValueError:
        print("\n An invalid entry occurred, closing program...")
        sys.exit(0)

# this function is called when the user wants to see the list of books. 
def show_books(_cursor):

    # collects book information from the book table.
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    # sets the results of the above query equal to the books variable.
    books = cursor.fetchall()

    print("\n-- DISPLAYING BOOK LISTING --")

    # iterates through all the received data in the books variable.
    for book in books:
        print("Book Name: {}\nAuthor: {}\nDetails: {}\n".format(book[1], book[2], book[3]))

# this function is called when the user wants to show location(s) information.
def show_locations(_cursor):

    # pulls store_id and the location from the store table for all stores
    _cursor.execute("SELECT store_id, locale from store")

    # sets the locations variable equal to the data pulled above.
    locations = _cursor.fetchall()

    print("\n-- DISPLAYING STORE LOCATIONS --")

    # iterates through the locations data to display all the store entries.
    for location in locations:
        print("Locale: {}\n".format(location[1]))

# this function is called get the user's user_id and validate it to confirm if it is valid or not, and then returns the user_id if it is valid. 
# An error message is displayed and the program is ended if the user_id is not valid.
def validate_user():

    # checks to see if the entered value is valid or not.
    try:
        user_id = int(input("\nPlease enter your user ID: "))

        if user_id < 0 or user_id > 3:
            print("\nInvalid user ID, program terminated...\n")
            sys.exit(0)

        return user_id
    # if the entry is not valid (such as letters) this terminates the program.
    except ValueError:
        print("\nInvalid entry, program terminated...\n")
        sys.exit(0)

# this function shows the menu for a user with a valid user_id.
def show_account_menu():
    
    # checks to see if the menu option chosen is valid or not. 
    try:
        print("\n--Customer Menu --")
        print("\n1. Wishlist\n2. Add Book\n3. Main Menu")

        account_menu_option_chosen = int(input("Type in a number to choose a menu option: "))

        return account_menu_option_chosen

    # if the menu option chosen wasn't valid, this will run.
    except ValueError:
        print("\nInvalid menu option, program terminated...\n")
        sys.exit(0)

# this function can be called to view all the books in a user's wishlist.
def show_wishlist(_cursor, _user_id):

    #this cursor collects information from across multiple tables then uses two inner joins to display the matching information collected.
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON w…
