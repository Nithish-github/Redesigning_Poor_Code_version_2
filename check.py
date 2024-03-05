from storage import Storage

class check:

    """
    Manages the checkout process, including checking books out to users
    and processing returns.
    Used of Checking the avaliability of the book also

    In user dataset we are having a variable " "books_checked_out": []" to track the book avaliability
    """

    def __init__(self, storage: Storage):
        self.storage = storage

    def checkout_book(self, user_id, isbn):
        #CHECK OUT FUNCTION
        data = self.storage.load_data()
        books = data.get("books", [])
        users = data.get("users", [])

        book = next((book for book in books if book["isbn"] == isbn and book.get("availability", True)), None)
        if not book:
            print("Book not available for checkout.")
            return

        user = next((user for user in users if user["user_id"] == user_id), None)
        if not user:
            print("User not found.")
            return

        book["availability"] = False
        user.setdefault("books_checked_out", []).append(isbn)

        self.storage.save_data(data)
        print(f"Book {isbn} checked out to user {user_id}.")

    def checkin_book(self, isbn):
        #CHECK IN FUNCTION 
        data = self.storage.load_data()
        books = data.get("books", [])
        users = data.get("users", [])

        book = next((book for book in books if book["isbn"] == isbn), None)
        if not book or book.get("availability", False):
            print("Book not found or already checked in.")
            return

        book["availability"] = True

        for user in users:
            if isbn in user.get("books_checked_out", []):
                user["books_checked_out"].remove(isbn)
                break

        self.storage.save_data(data)
        print(f"Book {isbn} checked in.")


    def is_book_available(self, isbn):
        # Check if the specified book is available
        data = self.storage.load_data()
        users = data.get("users", [])

        book = next((book for book in data.get("books", []) if book["isbn"] == isbn), None)

        if book:
            print('Book is avaliable')
            for user in users:
                if isbn in user.get("books_checked_out", []):
                    print("Current checked out")
                    return   
            print("Currently avaliable for check out")
            return
        
        else:
            print("Book not found.")
            return