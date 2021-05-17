n=int(input("enter the no. of fibonacci series:"))
i=1
d1=0
d2=1
for i in range (i,n+1):
    print(d1)
    sum=d1+d2
    d1=d2
    d2=sum
