a = 10
b = 0

try:
    result = a / b
    print("Result:", result)
except ZeroDivisionError as e:
    print("Error:", e)


my_list = [1, 2, 3]

try:
    print(my_list[5])
except IndexError as e:
    print("Index Error:", e)

    
def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print("Error:", e)
    except TypeError as e:
        print("Type Error:", e)
    except Exception as e:
        print("Unexpected Error:", e)
    finally:
        print("Execution completed")


safe_divide(1, 0)     # ZeroDivisionError
safe_divide(1, "a")   # TypeError
