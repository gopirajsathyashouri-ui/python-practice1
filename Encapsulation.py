class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password 

    def get_password(self):
        return self.__password 
    def set_password(self, new_password):
        self.__password = new_password

user1 = User("rahul_123", "abc123")

print("Old Password:", user1.get_password())
user1.set_password("newpass456")

print("Updated Password:", user1.get_password())
