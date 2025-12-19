# utils.py
def log_method_call(func):
    """Decorator to log method calls"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

def data_generator(data):
    """Simple generator to lazily process data"""
    for item in data:
        yield item * 2
