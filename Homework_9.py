#1
class Animal:
    def __init__(self, name, kingdom, color):
        self.name = name
        self.kingdom = kingdom
        self.color = color

    def getInfo(self):
        print(f'The {self.name} belongs to the {self.kingdom} kingdom. It is {self.color}.')

    @staticmethod
    def action(action):
        print(f'This animal is {action}!')

    def class_to_dict(self):
        print(vars(self))


rabbit = Animal('rabbit', 'animals', 'grey')
rabbit.getInfo()
Animal.action('jumping')
rabbit.class_to_dict()


#2

class Employee:
    count = 0
    def __init__(self, name, salary, title):
        self.name = name
        self.salary = salary
        self.title = title
        Employee.count+=1
    @classmethod
    def totalEmpl(cls):
        total = cls.count
        return total
def getAllSalary(class_objects):
    salaries_list = [obj.salary for obj in class_objects]
    return sum(salaries_list)

def avgSalary(a, b):
    avgSalary = a/b
    return (avgSalary)

emp1 = Employee('Yulia', 1800, 'QA')
emp2 = Employee('Roman', 4800, 'BA')
emp3 = Employee('Alex', 5300, 'Dev')
emp4 = Employee('Dmytro', 5000, 'Dev')
num = int(Employee.totalEmpl())
print(f'The total number of employees is {num}.')
employees_list = [emp1, emp2, emp3]
totalSalaries = getAllSalary(employees_list)
avgSalary = avgSalary(totalSalaries, num)
print(f'The average company salary is {avgSalary} $')

# 3
def funcName(func):
    def inner(*args, **kwargs):
        print(f'Function name is: {func.__name__}')
        return func(*args, **kwargs)
    return inner

@funcName
def total(a, b, c):
    totalSum = a + b + c
    print(totalSum)

total(4,8,8)

@funcName
def mult(a, b, c):
    mult = a * b * c
    print(mult)

mult(5,7,1)

#4

import random
myList = [random.randint(1, 10) for i in range(100)]
print(myList)
element_counts = {element: myList.count(element) for element in myList}
print(element_counts)