# #Q1
l = ['P1.py','first.txt','t3.py','tk.txt','tfk.com']
d ={}
for i in l:
    j = i.split('.')
    out = j[1]
    inn = j[0]

    if out not in d:
        d[out] =  []
    d[out].append(inn)
print(d)

# #Q2
inp = 'aaabbaabcc'
out = ''
count = 1

for i in range(len(inp)):
    if i < len(inp) - 1 and inp[i] == inp[i + 1]:
        count += 1
    else:
        out += inp[i] + str(count)
        count = 1

print(out)

# #Q3
l = ['aditya', 'archit', 'pradit', 'keshav']
v =''
for i in l:
    for j in i:
        if j in 'aeiouAEIOU':
            v+= j
print(v)
print(len((v)))

# #Q4
l = [(2+3j),12,'program','python',False]
d={}
for i in l:
    if type(i)==str:
        v=''
        for j in i:
            if j in 'aeiouAEIOU':
                v+=j
        d[i]=v
print(d)               

# #break statement
for i in range(1,11):
    print(i,end=' ')
    if(i==5):
        break

# #Pass keyword
for i in range(1,11):
    if i==5:
        pass
        print('hello')
