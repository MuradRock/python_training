class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Alice", 25)
print("Name:", p.name)
print("Age:", p.age)







class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print(f"Account balance: {self.balance}")


acc = BankAccount("123456", "John Doe", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.check_balance()


### class method

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split(", ")
        return cls(title, author)


book = Book.from_string("Python Programming, John Doe")
print("Title:", book.title)
print("Author:", book.author)


##method overriding

class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
        def sound(self):
            return "Meow"


dog = Dog()
cat = Cat()

print(dog.sound())
print(cat.sound())




##Multiple Inheritance
class Father:
    def skill(self):
        return "Carpentry"

class Mother:
    def hobby(self):
        return "Painting"

class Child(Father, Mother):
    pass


child = Child()
print(child.skill())   # inherited from Father
print(child.hobby())   # inherited from Mother



