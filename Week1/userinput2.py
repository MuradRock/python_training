names=input("Enter names separated by commas: ")
name_list=names.split(",")
list=[];
for name in name_list:
    name=name.strip()  # Remove leading/trailing whitespace
    list.append(name)



print("The names are: ", list)

new_list=[name.strip() for name in name_list]

print("The names are: ", new_list)

joined_names="; ".join(new_list)

print("Joined names: ", joined_names)
age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote.")

pi =3.14159
print(f"The value of pi is approximately {pi:.2f}")   