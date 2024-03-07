n = int (input(" enter the number "))
sum = 0
temp = n
while n != 0 :
    i = n % 10
    sum = sum * 10 + i
    n = n // 10
if sum == temp :
    print(" given number is palindrome")
else :
    print(" given number is notpalindrome")
