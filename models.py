#DEFINE THE DATA MODELS FOR BOOK AND USER CLASS
class Book:

    """
    Attributes:
        isbn (str): The International Standard Book Number uniquely identifying the book.
        title (str): The title of the book.
        author (str): The name of the book's author.

    The Book class is used to create instances of books with essential information
    that can be stored, retrieved, and managed within the library system.
    """
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author

class User:

    """
    Attributes:
        user_id (str): A unique identifier for the user.
        name (str): The name of the user.
        books_checked_out (list): A list of books currently checked out by the user.

    The User class is designed to keep track of users and their interactions with
    the library, such as checking out and returning books. It allows the system to
    manage user information and their borrowed book records.
    """
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_checked_out = []
