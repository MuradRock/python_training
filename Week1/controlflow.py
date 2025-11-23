

num=int(input('please enter number'))

if num %2 ==0:
    print('even')
else:
    print('odd')    


palindrome='civic'

reversed_str="".join(reversed(palindrome))

print(reversed_str)

rev=""

for ch in palindrome:
   rev=   ch+rev


print(rev)

if palindrome ==rev:
     print('it is palindrome')
else:
    print('not palindrom')    




