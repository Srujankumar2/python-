x = int(input("enter the number "))
temp = x
sum = 0
while x != 0 :
    i = x % 10
    sum = sum + i * i * i
    x = int(x / 10)
if sum == temp :
    print("given number is armstrong  ")
else :
    print("given number is not armstrong  ")
