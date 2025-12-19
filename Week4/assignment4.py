import time
from functools import wraps

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Executing {func.__name__} with args={args}, kwargs={kwargs}, took {execution_time:.4f} seconds.")
        return result
    return wrapper

def conditional_log(enable_logging=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if enable_logging:
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                execution_time = end_time - start_time
                print(f"Executing {func.__name__} with args={args}, kwargs={kwargs}, took {execution_time:.4f} seconds.")
            else:
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


class MyClass:
    @log_execution
    def method1(self, a, b):
        return a + b

    @conditional_log(enable_logging=True)
    def method2(self, x, y):
        return x * y

    @log_execution
    @conditional_log(enable_logging=False)
    def method3(self, p, q):
        return p - q

obj = MyClass()
print(obj.method1(3, 4))  
print(obj.method2(5, 6)) 
print(obj.method3(10, 5))  
