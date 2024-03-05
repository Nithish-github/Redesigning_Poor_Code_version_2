from storage import Storage

class user:
    """
    Handles operations related to users such as adding, updating, listing,
    and deleting users.
    """
    
    def __init__(self, storage: Storage):
        self.storage = storage

    def add_user(self, user):
        #FUNCTION TO ADD NEW USERS
        data = self.storage.load_data()
        users = data.get("users", [])
        users.append(user.__dict__)
        data["users"] = users
        self.storage.save_data(data)
        print(f"User {user.name} added successfully.")

    def list_users(self):
        #FUNCTION TO DISPLAY THE LIST OF USERS
        users = self.storage.load_data().get("users", [])
        if users:
            print("\nList of Users:")
            for user in users:
                print(f"User ID: {user['user_id']}, Name: {user['name']}")
        else:
            print("\nNo users available.")

    def delete_users(self, attribute, value):
        #FUNCTION TO DELETE BOOKS
        data = self.storage.load_data()
        users= data.get("users", [])
        updated_user = [user for user in users if user.get(attribute) != value]

        if len(users) == len(updated_user):
            print(f"No user found with {attribute}: {value}")
        
        else:
            #MAKING THE CHANGES ONLY TO THE BOOK DATA STRUCTURE
            data["users"] = updated_user
            self.storage.save_data(data)
            print(f"User with {attribute} : {value} deleted successfully")


    def search_users(self, attribute, value):
        #FUNCTION TO SEARCH USERS
        users = self.storage.load_data().get("users", [])
        matching_users = [user for user in users if user.get(attribute) == value]
        if not matching_users:
            print(f"No users found with {attribute}: {value}")
        else:
            print(f"Users found with {attribute}: {value}:")
            for user in matching_users:
                print(f"User ID: {user['user_id']}, Name: {user['name']}")

    def update_user(self, search_attribute, search_value, update_attribute, new_value):
            # FUNCTION TO UPDATE USER INFORMATION
            data = self.storage.load_data()
            users = data.get("users", [])
            updated = False
            for user in users:
                print(user.get(search_attribute))
                if user.get(search_attribute) == search_value:
                    user[update_attribute] = new_value
                    updated = True
            if updated:
                data["users"] = users  
                self.storage.save_data(data)
                print(f"User(s) with {search_attribute}: {search_value} have been updated. {update_attribute} set to {new_value}.")
            else:
                print(f"No user found with {search_attribute}: {search_value} to update.")