import json
import os

class Storage:

    """
    Provides file-based storage for persisting and retrieving library
    data including users, books, and checkouts.
    """

    def __init__(self, filename):
        self.filename = filename
        if not os.path.isfile(self.filename):
            # If the file does not exist, create an empty JSON structure
            print("\nFile storage not found")
            print("\nCreating file storage with {} name".format(filename))
            self.save_data({"books": [], "users": []})
        else:
            #If the storage , display the message
            print("\nFile storage {} found".format(filename))

    def save_data(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        # Check if the file exists
            # If the file exists, load its content
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except FileNotFoundError:
                return {}

