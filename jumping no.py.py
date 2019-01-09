r = int(input())
for k in range(r):
    n = int(input())
    
    b = list(str(n))
    c = [int(i) for i in b]
    
    print(c)
    b= False
    for i in range(0,len(c)-1):
        for j in range(i+1,len(c)-1):
            
            if (abs(c[i]-c[j])==1):
                b = True
            else:
                b = False
    print(b)
    
            