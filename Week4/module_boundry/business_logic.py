# business_logic.py

def process_data(data):
    """Business logic function that processes the data."""
    return sum(data)

def validate_data(data):
    """Simple data validation function."""
    if not isinstance(data, list):
        raise ValueError("Data should be a list.")
    return True
