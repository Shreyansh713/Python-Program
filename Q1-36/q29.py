n = int(input("Enter 3 Digit Number : "))
a = n%100
b = a%10 #last digit
c = a//10 #2nd digit
d = n//100

sum = b+c+d

print("Sum of 3 Digit Number","->",sum)