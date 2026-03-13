# class Bank:
#     balance=0
    
#     def createacc(self):
#         self.name=input('enter ur name: ')
#         self.acc=int(input('enter acc no.: '))
#         self.pin=int(input('enter the 4 digit pin: '))
#     def deposit(self):
#         name=input('enter ur name: ')
#         acc=int(input('enter acc no.: '))
#         amount=int(input('enter amount deposit: '))
#         pin=int(input('enter the 4 digit pin: '))
#         if name==self.name and acc==self.acc and pin==self.pin:
#             print('last balance:',balance)
#             balance+=amount
#         print('Success!!!','Current Balance: ',balance)

#     def withdraw():

#         name=input('enter ur name: ')
#         acc=int(input('enter acc no.: '))
#         amount=int(input('enter amount withdraw: '))
#         pin=int(input('enter the 4 digit pin: '))
#         if name==self.name and acc==self.acc and pin==self.pin:
#             print('last balance:',balance)
#             balance-=amount
#         print('Success!!!','Current Balance: ',balance)

#     def getbal(self):
#         print("current balance: ",self.balance)
# a=int(input(f"choose one: 1. Create new acc 2. Deposit amount 3. Withdraw Balance 4. Check Balance "))
# cust1=Bank()
# if a==1:
#     cust1.createacc()
# elif a==2:
#     cust1.deposit()
# elif a==3:
#     cust1.withdraw()
# elif a==4:
#     cust1.getbal()
# else:
#     print('invalid num')


# inheritance
class Car:
    def __init__(self, f_type):
        self.f_type = f_type
    
    @staticmethod
    def start():
        print("Car Started....")

    @staticmethod
    def stop():
        print("Car Stopped")


class Bmw(Car):
    def __init__(self, name, f_type):
        self.name = name
        super().__init__(f_type)
        super().start()


Car1 = Bmw('fortuner', 'petrol')

print(Car1.f_type)


#task
class Employee:
    
    def _init_(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):

    def _init_(self, name, salary, department):
        super()._init_(name, salary) 
        self.department = department

e1 = Manager("bxs", 11, "sk")
print(e1.department)
print(e1.name)
print(e1.salary)

    