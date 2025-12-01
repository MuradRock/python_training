numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]

max_value = max(numbers)
min_value = min(numbers)

print("Max:", max_value)
print("Min:", min_value)



setn = {5, 10, 3, 15, 2, 20}

max_value = max(setn)
min_value = min(setn)

print("Max:", max_value)
print("Min:", min_value)


def shortest_and_longest(words):
    shortest = min(words, key=len)
    longest = max(words, key=len)
    return (shortest, longest)

words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
result = shortest_and_longest(words)

print(result)  # ('kiwi', 'grapefruit')
