# user.py
import time
from collections import namedtuple

# User configuration (namedtuple)
Config = namedtuple('Config', ['host', 'port', 'debug'])

def execution_time(func):
    """Decorator to measure execution time of a function"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def access_control(required_role):
    """Decorator to check if the user has the required role"""
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if self.role != required_role:
                print(f"Access denied for user with role '{self.role}'. Required role: '{required_role}'")
                return None
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

class User:
    """Base class for user management with lifecycle and business logic"""

    def __init__(self, username, role, config):
        self.username = username
        self.role = role
        self.config = config
        self.__created_at = time.time()
        print(f"{self.username} created at {time.ctime(self.__created_at)}")

    def __str__(self):
        return f"User: {self.username}, Role: {self.role}"

    def __repr__(self):
        return f"User(username={self.username!r}, role={self.role!r}, config={self.config!r})"

    @execution_time
    def update_profile(self, new_info):
        """Update user profile (simulated)"""
        print(f"Updating profile for {self.username}...")
        time.sleep(1)  # Simulating time-consuming task
        return f"Profile updated to: {new_info}"

    def __del__(self):
        """Object lifecycle management (e.g., cleanup)"""
        print(f"User {self.username} is being deleted.")
    
    @access_control('admin')
    def delete_account(self, target_user):
        """Delete user account (only admin can delete)"""
        print(f"Deleting account for {target_user}")
        return f"Account for {target_user} deleted."

    def __call__(self):
        """Make the object callable, e.g., to return a greeting"""
        return f"Hello, {self.username}!"


class Admin(User):
    """Admin user class with extra privileges"""
    def __init__(self, username, config):
        super().__init__(username, role='admin', config=config)


class RegularUser(User):
    """Regular user class with standard privileges"""
    def __init__(self, username, config):
        super().__init__(username, role='user', config=config)


class ConfigManager:
    """Configuration manager for initializing user configurations"""
    def __init__(self):
        self.default_config = Config(host="localhost", port=8080, debug=True)
    
    def create_user(self, username, role):
        """Generate users based on their roles"""
        if role == "admin":
            return Admin(username, self.default_config)
        elif role == "user":
            return RegularUser(username, self.default_config)
        else:
            raise ValueError(f"Unknown role: {role}")
