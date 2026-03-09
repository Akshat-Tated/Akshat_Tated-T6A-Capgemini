# class College:
#     c_name = 'JECRC'
#     loc = 'Jaippur'

# #object creation
# s1 = College()
# print(s1)
# print(College)
# s1.name='Bhavik'

# s2=College()
# print(s1.name)
# print(s2.name)


#constructor

class Student:
    def __init__(self,name='Not Provided',
    student_id='Not Provided',
    branch='Not Provided'):
        self.name=name
        self.student_id=student_id
        self.branch=branch

s3=Student('Akshay','it190','cs')
print(s3.name,s3.student_id,s3.branch)

s1=Student()
s2=Student()
print(s1.name,s1.student_id,s1.branch)
print(s2.name,s2.student_id,s2.branch)

s1.name='Tushar'
s1.student_id='it176'
s1.branch='it'

s2.name='Akshat'
s2.student_id='cs177'
s2.branch='cs'

print(s1.name,s1.student_id,s1.branch)
print(s2.name,s2.student_id,s2.branch)

print(type(s2))



#example
# If function is defined in a class it is called methods
# Types of methods
    # 1. Object method - You can call it through object and class and make changes. If you change any CLASS PROPERTIES it will only change for that object only not for others. Like if you change location of e1 by this object method it will change location for e1 only not for others.

    # 2. Class method - But if you change CLASS PROPERTIES by class method, then it will get changed for all the other objects. (For understanding - it make changes in the main area(accessed by all objects), so it gets reflected in all other objects). 

    # 3. Static method - 

class Employee:
    company = "Capgemini"
    location = "Mumbai"
    childCompany = "Sogeti"

    def __init__(self, name, id, salary, department, age):
        self.name = name
        self.id = id
        self.salary = salary
        self.department = department
        self.age = age

    # Object method - We can call and access properties of class also    
    def display(self, company): 
        self.company = company 
        print(f"Name - {self.name}")
        print(f"id - {self.id}")
        print(f"Salary - {self.salary}")
        print(f"Company - {self.company}")
        print(f"Location - {self.location}")
        print(f"ChildCompany - {self.childCompany}")
        print(f"Department - {self.department}")
        print(f"Age - {self.age}")

    # Class method - 
    @classmethod
    def displayOnlyClassProperties(cls, company="Capgemini"):
        cls.company = company
        print(cls.company)
        print(cls.location)
        print(cls.childCompany)

    # Static method - Just a normal method
    @staticmethod
    def greeting(name):
        print(f"Ram Ram {name}")    

e1 = Employee("Ram", "ram@001", 1000000, "Creator", 10)
e2 = Employee("Ram1", "ram@001", 1000000, "Creator", 10)

# e1.display("hehe")
# print(e2.company)

# e1.displayOnlyClassProperties("hehe")
# print(e2.company)
# Employee.displayOnlyClassProperties("he")

# e1.greeting("Om")
# Employee.greeting("Om")

