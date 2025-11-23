nums = [1, 2, 3, 4, 5]
result = []

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == 9:
            result = [nums[i], nums[j]]



i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1


#break when searched number found
numbers = [10, 20, 30, 40, 50]
search_for = 30

for num in numbers:
    if num == search_for:
        print("Found:", num)
        break


#continue
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


for i in range(5):
    if i == 3:
        pass  
    print(i)




day = input("Enter a day: ").lower()

match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("It's a weekday")
    case "saturday" | "sunday":
        print("It's a weekend")
    case _:
        print("Invalid day")
