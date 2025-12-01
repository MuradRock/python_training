import time

def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Time taken: {end - start} seconds")
        return result
    return wrapper

@time_it
def append_numbers():
    my_list = []
    for i in range(1, 1001):
        my_list.append(i)
    return my_list

append_numbers()

###########retry

def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    print(f"Attempt {attempt}...")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}")
                    if attempt == times:
                        print("Max retries reached.")
        return wrapper
    return decorator


@retry(3)
def may_fail(name):
    print(f"Hello, {name}!")

may_fail("Murad")


#### validate positive

def validate_positive(func):
    def wrapper(x):
        if x <= 0:
            raise ValueError("Value must be positive!")
        return func(x)
    return wrapper


@validate_positive
def square_root(x):
    return x ** 0.5

print(square_root(16))
# print(square_root(-4))  # This will raise ValueError


### cache

def cache(func):
    stored_results = {}

    def wrapper(x):
        if x in stored_results:
            print("Returning cached result...")
            return stored_results[x]

        print("Performing computation...")
        result = func(x)
        stored_results[x] = result
        return result

    return wrapper


@cache
def expensive_computation(x):
    return x * x


print(expensive_computation(5))   # Computation happens
print(expensive_computation(5))   # Cached result


### permission

def requires_permission(func):
    def wrapper(user, *args, **kwargs):
        if 'admin' in user.get('permissions', []):
            return func(user, *args, **kwargs)
        else:
            print("Access denied")
    return wrapper


@requires_permission
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")


user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test']}

delete_user(user1, 101)   # Allowed
delete_user(user2, 102)   # Access denied
delete_user(user3, 103)   # Access denied





