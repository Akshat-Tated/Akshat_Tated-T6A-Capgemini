# n = eval(input("Enter value :"))
# for i in range(1,4):
#     for j in range(1,5):
#         print('*',end=' ')
#     print()

# Task 1
# row = eval(input("Enter row :"))
# col = eval(input("Enter col :"))
# for i in range(0,row):
#     for j in range(0,col):
#         print('#',end=' ')
#     print()

# for i in range(0,4):
#     for j in range(0,4):
#         if(i == j):
#             print('@',end=' ')
#         else:
#             print('*',end=' ')
#     print()


# Lower Triangle => i > j
# Upper Trianle => i < j
# Primary Diagonal => i==j

#Task 2
# for i in range(0,4):
#     for j in range(0,4):
#         if(i == j):
#             print('*',end=' ')
#         elif(i > j):
#             print('#',end=' ')
#         elif(i < j):
#             print('@',end=' ')
#     print()

# row = eval(input("Enter row :"))
# col = eval(input("Enter col :"))
# for i in range(1,row+1):
#     for j in range(1,col+1):
#         if(i+j == row+1):
#             print('$',end=' ')
#         # if(i == j):
#         #     print('*',end=' ')
#         # elif(i > j):
#         #     print('#',end=' ')
#         # elif(i < j):
#         #     print('@',end=' ')
#         else:
#             print('1',end=' ')
#     print()


#task 3
row = eval(input("Enter row :"))
col = eval(input("Enter col :"))
for i in range(1,row):
    