class Employee:
    def __init__(self, fname, lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay


class Developer(Employee):
    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print(f"---> {emp.fname} {emp.lname}")        

dev1 = Developer("John", "Doe", 60000, "Python")
print(f"Developer: {dev1.fname} {dev1.lname}, Pay: {dev1.pay}, Programming Language: {dev1.prog_lang}")

mgr1 = Manager("Jane", "Smith", 90000, [dev1])
print(f"Manager: {mgr1.fname} {mgr1.lname}, Pay: {mgr1.pay}")
mgr1.print_employees()
mgr1.add_employee(Employee("Emily", "Davis", 50000))
print("After adding a new employee:")
mgr1.print_employees()  

print(isinstance(dev1, Employee))  # True
print(issubclass(Developer, Employee))  # True

print(issubclass(Manager, Developer))  # False
print(issubclass(Manager, Employee))  # True
