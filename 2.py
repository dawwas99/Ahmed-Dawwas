class User:
    user_id = 0

    def __init__(self, name, password):
        User.user_id += 1
        self.id = User.user_id
        self.name = name
        self.password = password

@staticmethod
    def user_info(self):
        print(f"ID Variabele : {User.user_id}")


user1 = User("Ahmed", 123456)
user2 = User("sara", 123456)
user3 = User("lana", 123456)

print(user1.id, ":", user1.name)
print(user2.id, ":", user2.name)
print(user3.id, ":", user3.name)

User.user_info()
