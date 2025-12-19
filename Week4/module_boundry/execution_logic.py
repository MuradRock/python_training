# execution_logic.py

from business_logic import process_data, validate_data

def run():
    """Execution logic that interacts with the business logic."""
    try:
        data = [1, 2, 3, 4, 5] 
        validate_data(data)  
        result = process_data(data)
        print(f"Processed Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
