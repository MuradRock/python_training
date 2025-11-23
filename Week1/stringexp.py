message=""" this is multi line 
string and it is end here"""
print(message)

print(len(message))
print(message[0])

print(message[0:5])
print(message[:5]) # from start till 5th
print(message[6:]) #from 6 to end

print(message.lower())
print(message.upper())

print(message.count('is')) #occurance
print(message.find('l')) # start index, -1 if not exists


greeting='hello'
name='Murad'

new_massage='{},{}. Welcome!.'.format(greeting,name)
print(new_massage)

# after python 3.6 you can use f string 

f_message=f'{greeting},{name.upper()}. Welcome!.'

print(f_message)
