from models import Book, User
from storage import  Storage
from book import book as book_management
from user import user as  user_management
from check import check as check_management
import logging



class main:
    
    '''
    main class orchestrates the interactions between different
    components of the library management system including books, users,
    and checkout processes.
    '''

    def __init__(self,filename):
        #CONSTRUCTOR FUNCTION

        #CHECKING FOR FILE STORAGE
        logger.info("Library Management System Started")
        print('Library Management System Started')
        print('\nLooking for file storage')
        storage = Storage("file_storage/"+str(filename)+".json")

        #CREATING THE OBJECT FOR BOOK MANAGEMENT
        self.book_manager = book_management(storage)

        #CREATING THE OBJECT FOR USER MANAGEMENT
        self.user_manager = user_management(storage)

        #CREATING THE OBJECT FOR CHECK OUT AND CHECK IN MANAGEMENT
        self.check_manager = check_management(storage)


    '''
    Following will be events to handle book operations
    '''

    def add_book_interface(self):
        #FUNCTION FOR ADDING THE BOOK

        title = input("\nEnter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        book = Book(isbn,title,author)
        self.book_manager.add_book(book)
        logger.info(f"New book with Title: {title}, author: {author}, isbn: {isbn} added")

    def list_books_interface(self):
        #FUNCTION FOR SHOWING THE LIST OF BOOKS

        self.book_manager.list_books()
        logger.info(f"Displaying the List of books avaliable")


    def delete_books_interface(self):
        #FUNCTION FOR SHOWING THE DELETING BOOKS

        print("\nDelete Book with")
        print("1. Title")
        print("2. Author")
        print("3. ISBN")
        print("4. BACK")

        choice = input("\nEnter choice (1-4): ")
        
        #DELETE THE RECORD WITH TITLE
        if choice == "1":
            value = input("\nEnter the Title: ")
            self.book_manager.delete_book('title',value)

        elif choice == '2':
            value = input("\nEnter the Author: ")
            self.book_manager.delete_book('author',value)

        elif choice == '3':
            value = input("\nEnter the ISBN: ")
            self.book_manager.delete_book('isbn',value)

        elif choice == 4:
            pass

        else:
            print("Invalid Choice")

        try:
            logger.info(f"Deleting the books with {value} identification")
        except:
            logger.info(f"Returing from Deleting")



    def search_books_interface(self):
        #FUNCTION FOR SHOEWING THE SEARCHED BOOKS

        print("\nSearch Book with")
        print("1. Title")
        print("2. Author")
        print("3. ISBN")
        print("4. BACK")

        choice = input("\nEnter choice (1-4): ")
        
        #DELETE THE RECORD WITH TITLE
        if choice == "1":
            value = input("\nEnter the Title: ")
            self.book_manager.search_books('title',value)

        elif choice == '2':
            value = input("\nEnter the Author: ")
            self.book_manager.search_books('author',value)

        elif choice == '3':
            value = input("\nEnter the ISBN: ")
            self.book_manager.search_books('isbn',value)

        elif choice == 4:
            pass

        else:
            print("Invalid Choice")

        try:
            logger.info(f"Searched the books with {value} identification")
        except:
            logger.info(f"Returing from searching")


    def update_books_interface(self):
        #FUNCTION FOR UPDATING THE BOOKS

        print("\nFor Updating select Book with")
        print("1. Title")
        print("2. Author")
        print("3. ISBN")
        print("4. BACK")
        choice_select = input("\nEnter choice (1-4): ")

        search_attribute = ''
        if choice_select == '1':
            search_attribute = 'title'
        elif choice_select == '2':
            search_attribute = 'author'
        elif choice_select == '3':
            search_attribute = 'isbn'
        elif choice_select == '4':
            return
        else:
            print("Invalid Choice")
            return

        search_value = input(f"\nEnter the {search_attribute.capitalize()}: ")

        print("\nUpdate Book with")
        print("1. Title")
        print("2. Author")
        print("3. ISBN")
        print("4. BACK")
        choice_update = input("\nEnter choice (1-4): ")

        update_attribute = ''
        if choice_update == '1':
            update_attribute = 'title'
        elif choice_update == '2':
            update_attribute = 'author'
        elif choice_update == '3':
            update_attribute = 'isbn'
        elif choice_update == '4':
            return
        else:
            print("Invalid Choice")
            return

        new_value = input(f"\nEnter the new {update_attribute.capitalize()}: ")

        #CALL BOOK MANAGER WITH THE UPDATE PARAMETER
        self.book_manager.update_book(search_attribute, search_value, update_attribute, new_value)

        try:
            logger.info(f"Updated the books with {new_value} identification")
        except:
            logger.info(f"Returing from update")


    '''
    Following will be events to handle users operations
    '''

    def add_user_interface(self):
        #FUNCTION FOR ADDING THE USER

        name = input("\nEnter user name: ")
        user_id = input("Enter user ID: ") 
        user = User(user_id,name)
        self.user_manager.add_user(user)
        logger.info(f"New user is created with name: {name},user ID: {user_id}")


    def list_user_interface(self):
        #FUNCTION FOR SHOWING THE LIST OF BOOKS

        self.user_manager.list_users()
        logger.info(f"Displaying the Users list")


    def delete_user_interface(self):
        #FUNCTION FOR SHOWING THE DELETING BOOKS

        print("\nDelete user with")
        print("1. name")
        print("2. user ID")
        print("3. BACK")

        choice = input("\nEnter choice (1-4): ")
        
        #DELETE THE RECORD WITH TITLE
        if choice == "1":
            value = input("\nEnter the name: ")
            self.user_manager.delete_users('name',value)

        elif choice == '2':
            value = input("\nEnter the user ID: ")
            self.user_manager.delete_users('user_id',value)

        elif choice == 3:
            pass

        else:
            print("Invalid Choice")


        try:
            logger.info(f"Deleting the user with {value} identification")
        except:
            logger.info(f"Returning from Deleting")



    def search_user_interface(self):
        #FUNCTION FOR SHOEWING THE SEARCHED USERS

        print("\nSearch user with")
        print("1. name")
        print("2. user ID")
        print("3. BACK")

        choice = input("\nEnter choice (1-3): ")
        
        #DELETE THE RECORD WITH TITLE
        if choice == "1":
            value = input("\nEnter the name: ")
            self.user_manager.search_users('name',value)

        elif choice == '2':
            value = input("\nEnter the user ID: ")
            self.user_manager.search_users('user_id',value)

        elif choice == 3:
            pass

        else:
            print("Invalid Choice")
            
        try:
            logger.info(f"Searching the user with {value} identification")
        except:
            logger.info(f"Returning from Searching")



    def update_user_interface(self):
        #FUNCTION FOR UPDATING THE USERS

        print("\nFor updating select user with")
        print("1. name")
        print("2. user ID")
        print("3. BACK")
        choice_select = input("\nEnter choice (1-3): ")

        search_attribute = ''
        if choice_select == '1':
            search_attribute = 'name'
        elif choice_select == '2':
            search_attribute = 'user_id'
        elif choice_select == '3':
            return
        else:
            print("Invalid Choice")
            return

        search_value = input(f"\nEnter the {search_attribute.capitalize()}: ")

        print("\nUpdate user with")
        print("1. name")
        print("2. user ID")
        print("3. BACK")
        choice_update = input("\nEnter choice (1-3): ")

        update_attribute = ''
        if choice_update == '1':
            update_attribute = 'name'
        elif choice_update == '2':
            update_attribute = 'user_id'
        elif choice_update == '3':
            return
        else:
            print("Invalid Choice")
            return

        new_value = input(f"\nEnter the new {update_attribute.capitalize()}: ")

        #CALL BOOK MANAGER WITH THE UPDATE PARAMETER
        self.user_manager.update_user(search_attribute, search_value, update_attribute, new_value)

        try:
            logger.info(f"Updating the user with {new_value} identification")
        except:
            logger.info(f"Returing from updating")



    def checkout_book_interface(self):

        user_id = input("\nEnter user_id: ")
        isbn = input("Enter ISBN: ")
        self.check_manager.checkout_book(user_id,isbn)

        logger.info(f"Cheking out the book with user_id: {user_id}, isbn: {isbn} identification")



    def checkin_book_interface(self):

        isbn = input("Enter ISBN: ")
        self.check_manager.checkin_book(isbn)

        logger.info(f"Cheking in the book with isbn: {isbn} identification")



    def check_book_availability(self):

        isbn = input("Enter ISBN: ")
        self.check_manager.is_book_available(isbn)

        logger.info(f"Cheking the avaliability of isbn: {isbn} book")




    def main_menu(self):
        print("\n**BOOK OPERATIONS**\n")
        print("1. Add Book")
        print("2. List Books")
        print("3. Delete Books")
        print("4. Search Books")
        print("5. Update Books")
        print("\n**USER OPERATIONS**\n")
        print("6. Add User")
        print("7. List Users")
        print("8. Delete Users")
        print("9. Search Users")
        print("10. Update Users")
        print("\n**CHECK IN/OUT OPERATIONS**\n")
        print("11. Check Out")
        print("12. Check In")
        print("13. Check Book Avaliability")
        print("14. Exit")
        choice = input("Enter choice (1-11): ")
        return choice

    def main_function(self):

        actions = {
            '1': self.add_book_interface,
            '2': self.list_books_interface,
            '3': self.delete_books_interface,
            '4': self.search_books_interface,
            '5': self.update_books_interface,

            '6': self.add_user_interface,
            '7': self.list_user_interface,
            '8': self.delete_user_interface,
            '9': self.search_user_interface,
            '10': self.update_user_interface,

            '11': self.checkout_book_interface,
            '12': self.checkin_book_interface,
            '13': self.check_book_availability,

        }
        while True:
            choice = self.main_menu()
            action = actions.get(choice)
            if action:
                action()
            elif choice == '14':
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":

    '''
    Local function 
    In this the basics log function is initialized
    Log for both File Handler is being initialized

    Object is created for library_management_system class
    main function of the object is getting executed
    '''

    #LOG OBJECT CREATION
    logger = logging.getLogger('LibraryManagement')
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler('logs/library_management.log')
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    #disabling the log to display on terminal 
    #since our approch is CLI making the terminal look neat.
    logger.propagate = False

    #LIBRARY MANAGEMENT SYSTEM OBJECT CREATION
    #file named 'storage' is passed , if required new name can be passed to create new file-storage 
    library_object = main("storage")

    #EXECUTING THE MAIN FUNCTION
    library_object.main_function()

