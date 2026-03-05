#Check if number is a 3-digit number or not take user input.
a = eval(input("Enter a number: "))
if a >= 100 and a <= 999:
    print("The number is a 3-digit number.")
else:
    print("The number is not a 3-digit number.")    

#Check if string length is greater than 5.
b = input("Enter a string: ")
if len(b) > 5:
    print("The string length is greater than 5.")
else:
    print("The string length is not greater than 5.")   

#Check if number is zero so print ‘zero’ otherwise print ‘Not Zero’.
c = eval(input("Enter a number: "))
if c == 0:
    print("zero")
else:
    print("Not Zero")

#Check if person can enter club (age + ID check). If yes, print ‘Eligible’.
age = eval(input("Enter age: "))
id = input("Enter ID: ")
if age >= 18 and id == "valid":
    print("Eligible")
else:
    print("Not Eligible")

#Check if number is within range 10–50 if yes print ‘In Range’ otherwise ‘Not in Range’.
num = eval(input("Enter a Number : "))
if num <= 50 and num >=10 :
    print("In Range")
else:
    print("Not in range")