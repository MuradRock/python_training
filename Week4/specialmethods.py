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
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA0-9-.]+$'
        return re.match(pattern, email) is not None

    @classmethod
    def get_active_users_count(cls):
        return cls.active_users_count

    def __del__(self):
        User.active_users_count -= 1

    def __str__(self):
        return f"User: {self.name}, Email: {self.email}"

    def __repr__(self):
        return f"User(name={self.name!r}, email={self.email!r})"

    def __len__(self):
        return len(self.name)  

    def __eq__(self, other):
        if isinstance(other, User):
            return self.email == other.email
        return False

    def __lt__(self, other):
        if isinstance(other, User):
            return len(self.name) < len(other.name)
        return False

    def __call__(self):
        """Make the object callable, for example, return a greeting."""
        return f"Hello, {self.name}!"


user1 = User("Alice", "alice@example.com")
user2 = User("Bob", "bob@example.com")
user3 = User("Charlie", "charlie@example.com")

print(str(user1))  
print(repr(user1))  
print(len(user1))  
print(user1 == user2)  
print(user2 == User("Bob", "bob@example.com"))  

print(user1 < user2)  

print(user1())  
