r = int(input())
for j in range(r):
    n = int(input())
    b = []
    x=1
    y=1
    for i in range(n+1):
        b.append(x)
        y=y+1
        x=x+y     
    if n in b:
        print("1")
    else:
        print("0")