fruits= ["apple", "banana", "cherry"]
for index,fruit in enumerate(fruits):
      print(f"{index} {fruit}")


person={"name": "Alice", "age": 30, "city": "New York"}

for key,value in person.items():
    print(f"{key}: {value}")

# Using list comprehension with enumerate to print index and fruit for even indices      
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print("Fruits at even indices:=================================")

even_indexed_fruits = [(index,fruit) for index, fruit in enumerate(fruits,start=1) if index %2==0]
print(even_indexed_fruits)