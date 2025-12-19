# main.py
from user import User, Admin, RegularUser, ConfigManager
from utils import data_generator, log_method_call

def run():
    """Main application logic that uses the above components."""
    config_manager = ConfigManager()

    # Create users
    admin = config_manager.create_user("admin_user", "admin")
    regular_user = config_manager.create_user("regular_user", "user")

    print(f"Created: {admin}")
    print(f"Created: {regular_user}")

    print(admin.update_profile("Admin profile updated"))
    print(regular_user.update_profile("Regular user profile updated"))

    admin.delete_account("regular_user")
    regular_user.delete_account("admin_user") 

    print(admin())  

    data = [1, 2, 3, 4, 5]
    print("Processing data using generator:")
    for value in data_generator(data):
        print(f"Processed value: {value}")

    del admin
    del regular_user

if __name__ == "__main__":
    run()
