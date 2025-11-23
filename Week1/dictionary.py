
student={'name':'murad','age':34,'cources':['math','science']}

print(student['cources'])

#print(student['mobile']) ## will throw error for not exist key

print(student.get('mobile'))
print(student.get('mobile','not found'))

student['phone']=8384838434
student['name']='Azlan' #it will update previous value
student.update({'name':'Alex','age':40}) #or we can use update method

print(student)

del student['age']
print(student)

removed_var=student.pop('phone')

print('removed var ',removed_var)

print(len(student))

print(student.keys())
print(student.values())
print(student.items()) ## if you want to print keys and values

for key in student:
 print(key)

for key,value in student.items():
   print(key,' , ',value) 


person = {"name": "Alice", "age": 30, "city": "New York"}

person['gender']='M'
print(person)

del person['city']


dict1 = {"a": 1, "b": 2}    
dict2 = {"c": 3, "d": 4,"b":5}

dict3=dict1 | dict2
print(dict3)

unpack_dict={**dict1, **dict2} # unpack 

print(unpack_dict)

dict1.update(dict2) # in place merged





