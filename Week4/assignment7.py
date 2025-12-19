def search_item(collection, target):
    """Search for an item in a collection and use 'else' when not found."""
    for item in collection:
        if item == target:
            print(f"Item '{target}' found!")
            break
    else:
        print(f"Item '{target}' not found in the collection.")

collection = [1, 2, 3, 4, 5]

search_item(collection, 3)  

search_item(collection, 10)  
