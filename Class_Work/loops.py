#numbers from 40 - 50 in reverse order
a= 50
while a>=40:
    print(a)
    a = a-1

#first 20even number
i = 0
count = 1
while count <=20:
    print(i)
    i +=2
    count +=1

#reverse a number
num = eval(input("Enter a number to reverse : "))
newnum = 0
while num > 0:
    last_digit = num%10
    newnum = (10*newnum) + last_digit
    num = num//10
print(newnum)

#WAP to print multiplication table of n
n = int(input("Enter n number : "))
count = 1
while count<=10:
    # print(n,' X ',count,' : ',n*count)
    print(f"{n}x{count}={n*count}")
    count +=1

#for loop

set1 = {2,3,4,5,6}
for i in set1:
    print(i)

for i in range(10,0,-1):
    print(i,end=' ')

# WAP to replace a space with underscore
name = "Akshat Tated"
newname = ''
for i in name:
    if i==" ":
        newname = newname+'_'
    else:
        newname = newname + i
print(newname)


