a=int(input("enter"))
tot=0
while(a>0):
    n=a%10
    tot=tot+n
    a=a//10
print(tot)