# Принципы SOLID
# Принцип единственной ответственности

class UserManager():
    def __init__(self, user):
        self.user = user

    def change_user_name(self, new_name):
        self.user.name = new_name

    def save_user(self):
        file = open("users.txt", "a")
        file.write(self.user)
        file.close()


class User():
    def __init__(self, name):
        self.name = name

class UserNameChanger():
    def __init__(self, user):
        self.user = user

    def change_user_name(self, new_name):
        self.user.name = new_name

class SaveUser():
    def __init__(self, user):
        self.user = user

    def save_user(self):
        file = open("users.txt", "a")
        file.write(self.user)
        file.close()