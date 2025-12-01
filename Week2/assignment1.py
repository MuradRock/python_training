nums=[1,2,3,4,5]
squared=list(map(lambda x:x**2,nums))
print(squared)

#filter
eve_nums=list(filter(lambda x:x%2==0,nums))
print(eve_nums)

#reduce
words = ["apple", "banana", "cherry", "date"]
from functools import reduce
longest_word= reduce(lambda acc, curr: acc if len(acc)>len(curr)  else curr, words)
print(longest_word)


#map
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
rounded = list(map(lambda x: round(x,1), my_floats))
print(rounded)

#filter names with less than 7 characters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
filterd_names = list(filter(lambda name: len(name)<7, my_names))
print(filterd_names)

#reduce to find sum of numbers
sum=reduce(lambda acc,curr:acc+curr,nums)
print(sum)
