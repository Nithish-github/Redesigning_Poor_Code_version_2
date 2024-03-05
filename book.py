from storage import Storage

class book:

    """
    Manages book-related operations including adding, updating, listing,
    and deleting books from the library's catalog.
    """

    def __init__(self, storage: Storage):
        self.storage = storage

    def add_book(self, book):
        #FUNCTION TO ADD NEW BOOKS

        data = self.storage.load_data()
        books = data.get("books", [])

        #TO CHECK THE AVALIABILITY OF THE BOOK

        book_dict = book.__dict__
        book_dict["availability"] = True 
        books.append(book_dict)

        #MAKING THE CHANGES ONLY TO THE BOOK DATA STRUCTURE

        data["books"] = books  
        self.storage.save_data(data)

        print("\nBook added successfully.")


    def list_books(self):
        #FUNCTION TO DISPLAY THE LIST OF BOOKS 
        books = self.storage.load_data().get("books", [])
        if books:
            print("\nList of Books:")
            for book in books:
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
        else:
            print("\nNo books available.")

    def delete_book(self, attribute, value):
        #FUNCTION TO DELETE BOOKS
        data = self.storage.load_data()
        books = data.get("books", [])
        updated_books = [book for book in books if book.get(attribute) != value]

        if len(books) == len(updated_books):
            print(f"No book found with {attribute}: {value}")
        else:
            #MAKING THE CHANGES ONLY TO THE BOOK DATA STRUCTURE
            data["books"] = updated_books
            self.storage.save_data(data)
            print(f"Book with {attribute} : {value} deleted successfully")


    def search_books(self, attribute, value):
        #FUNCTION TO SEARCH BOOKS
        books = self.storage.load_data().get("books", [])
        matching_books = [book for book in books if book.get(attribute) == value]
        if not matching_books:
            print(f"No books found with {attribute}: {value}")
        else:
            print(f"Books found with {attribute}: {value}:")
            for book in matching_books:
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")

    def update_book(self, search_attribute, search_value, update_attribute, new_value):
        #FUNCTION TO UPDATE THE BOOKS VALUES
        data = self.storage.load_data()
        books = data.get("books", [])
        updated = False
        for book in books:
            if book.get(search_attribute) == search_value:
                book[update_attribute] = new_value
                updated = True
        if updated:
            data["books"] = books
            self.storage.save_data(data)
            print(f"Book(s) with {search_attribute}: {search_value} have been updated. {update_attribute} set to {new_value}.")
        else:
            print(f"No book found with {search_attribute}: {search_value} to update.")
