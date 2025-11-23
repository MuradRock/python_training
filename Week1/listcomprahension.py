
#Convert list of numeric strings → integers
strings = ["1", "2", "3", "4", "5"]
result = [int(x) for x in strings]
print(result)

#Extract integers greater than 10

numbers = [1, 5, 13, 4, 16, 7]
result = [n for n in numbers if n > 10]
print(result)


#List of squares from 1 to 5

result = [x*x for x in range(1, 6)]
print(result)
#Convert 2D list → 1D list

matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
result = [item for row in matrix for item in row]
print(result)


#Create dictionary from two lists

keys = ['a', 'b', 'c']
values = [1, 2, 3]

result = {k: v for k, v in zip(keys, values)}
print(result)


#New dictionary with students scoring above 80
scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}

result = {name: score for name, score in scores.items() if score > 80}
print(result)





