import re

class User:
    active_users_count = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.active_users_count += 1

    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}")

    @classmethod
    def from_serialized(cls, serialized_str):
        """Creates an instance from a serialized string."""
        name, email = serialized_str.split(",") 
        name = name.strip()
        email = email.strip()
        if not cls.validate_email(email):  
            raise ValueError("Invalid email format!")
        return cls(name, email)

    @staticmethod
    def validate_email(email):
        """Validates the email format using regex."""
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    @classmethod
    def get_active_users_count(cls):
        return cls.active_users_count

    def __del__(self):
        User.active_users_count -= 1

try:
    userlist = "Alice, alice@example.com"
    user1 = User.from_serialized(userlist)
    user1.display_info()
    print(f"Active Users: {User.get_active_users_count()}")
    
    invalid_serialized_user = "Bob, bob@invalid"
    user2 = User.from_serialized(invalid_serialized_user)
except ValueError as e:
    print(f"Error: {e}")

print(f"Active Users after error: {User.get_active_users_count()}")
