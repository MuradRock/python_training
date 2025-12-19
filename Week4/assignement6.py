from collections import namedtuple

Config = namedtuple('Config', ['host', 'port', 'debug'])

class ConfigManager:
    def __init__(self):
        self.config = Config(host="localhost", port=8080, debug=True)
    
    def get_config(self):
        """Retrieve the current configuration"""
        return self.config
    
    def set_config(self, host, port, debug):
        """Create a new configuration object, demonstrating immutability"""
        self.config = Config(host=host, port=port, debug=debug)

manager = ConfigManager()

current_config = manager.get_config()
print(f"Current Config: {current_config}")

try:
    current_config.host = "127.0.0.1" 
except AttributeError as e:
    print(f"Error: {e}")

manager.set_config("127.0.0.1", 9090, False)
new_config = manager.get_config()
print(f"New Config: {new_config}")
