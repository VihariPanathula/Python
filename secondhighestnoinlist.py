a=[97,1,2,33,44,65,65,97,97,1]
b=[]
for i in a:
    if i not in b:
        b.append(i)
b.sort()
print(b[-2])
