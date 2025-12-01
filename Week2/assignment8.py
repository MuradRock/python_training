with open("sample.txt", "r") as file:
    content = file.read()
    print(content)



with open("words.txt", "r") as file:
    text = file.read()
    words = text.split()
    print("Number of words:", len(words))



#write to a file
with open("output.txt", "w") as file:
    file.write("Hello, Python!")
   


import csv

data = [
    ["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]
]


with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("students.csv created successfully!")


## Generator to read large file line by line

def read_lines(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()


# Example usage:
for line in read_lines("bigfile.txt"):
    print(line)






