n=eval(input("enter the number "))
sp=0
sn=0
countn=0
countp=0
while(n!=-1):
    if(n>0):
        countp+=1
        sp=sp+n
else:
    countn+=1
    sn=sn+n
n=eval(input("enter a number"))
print("avarge of negative is",sn/countn)
print("avarge of postitive is",sp/countp)
