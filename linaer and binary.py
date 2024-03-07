a=eval(input("enter the list:"))
print(a)
b=sorted(a)
def linear_search(b):
    search=eval(input("enter a element to search:" ))
    for i in range (0,len(b),1):
        if(search==b[i]):
            print("element found at " ,i+1)
            break
    else:
            print("not found")
def binary_search(b):
    search=eval(input("enter a element to search:" ))
    start=0
    stop=len(a)-1
    print(b)
    while(start<=stop):
       mid=(start+stop)//2
       if(search==b[mid]):
             print("elemrnt found at",mid+1)
             break
       elif(search<b[mid]):
             stop=mid-1
       elif(search>b[mid]):
             start=mid+1
    else:
       print("not found")
n=eval(input("enter 1 for linear search and 2 for binary search:"))
if(n==1):
    linear_search(b)
elif(n==2):
    binary_search(b)
else:
    print("no search operation performed")
