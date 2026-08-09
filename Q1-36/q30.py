n = int(input("Enter 4 Digit Number : "))

a = n%1000
b = a%100
c = b%10 #last 
d = b//10 #2nd digit
e = a//100 #3rd digit
f = n//1000 #4th digit

product = f*e*d*c

print(product)