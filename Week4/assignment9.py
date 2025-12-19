import time

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

def log_method_call(func):
    """Decorator to log method calls"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    @execution_time
    @log_method_call
    def update_profile(self, new_info):
        """Update user profile"""
        print(f"Updating profile for {self.username}")
        time.sleep(1)  # Simulating some time-consuming task
        return f"Profile updated to: {new_info}"

    @access_control('admin')  # Only users with 'admin' role can delete accounts
    @log_method_call
    def delete_account(self, target_user):
        """Delete a user account"""
        print(f"Deleting account for {target_user}")
        return f"Account for {target_user} deleted."


class Admin(User):
    def __init__(self, username):
        super().__init__(username, role='admin')


class RegularUser(User):
    def __init__(self, username):
        super().__init__(username, role='user')


# Test execution
admin = Admin("admin_user")
regular_user = RegularUser("regular_user")

# Test update_profile (execution time and logging)
admin.update_profile("New admin info")
regular_user.update_profile("New regular user info")

# Test delete_account (logging and access control)
admin.delete_account("regular_user")
regular_user.delete_account("admin_user")  # This should be denied due to access control
