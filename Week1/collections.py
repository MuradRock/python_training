names=["Murad","Ali","Adeeba","Azlan"]

print(len(names))

numbers=[1,8, 2,10, 3, 4, 5]

print(min(numbers))
print(max(numbers)) #sum() is also there
numbers.reverse()
print(numbers)

numbers.sort(reverse=True) #sort in reverse order
print(numbers)

new_numbers=sorted(numbers)# sort list in new list not in place

print(new_numbers)
print(numbers)

print(numbers.index(10))

print(2 in numbers)

for index, num in enumerate(numbers,start=1):
  print(index,' ',num)

print("*".join(names))
print(numbers.count(10))



