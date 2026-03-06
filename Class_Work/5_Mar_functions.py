# inp1 = eval(input("enter 1st val : "))
# inp2 = eval(input("enter 2nd val : "))

# def prod(inp1,inp2):
#     print(inp1*inp2)

# prod(inp1,inp2)

# without input
# def product():
#     a = int(input())
#     b = int(input())
#     print(a*b)

# product()

# l = eval(input("Emter a list:"))
# l2 =[]
# def extract_negative():
#     for i in l:
#         if i < 0:
#             l2.append(i)
#     return l2
# print(extract_negative())


a=3
# for i in range(1,3):
#     a += 2
def changeval():
    global a
    t = 9
    a = 1
    def cval():
        nonlocal t
        t = 55
changeval()
print(a)

#Main and important inbuild functions of DSs-

# String - upper, lower, swapcase, replace, capitalize, title, split, join, index, count, isupper, islower, isdigit, rstrip, lstrip, strip.

# List - append, insert, pop, remove, sort, reverse, count, index.

# Set - add, pop, remove, union, intersection, difference, clear, update.

# Dict- keys, values, items, get, pop, popitems, update, clear.