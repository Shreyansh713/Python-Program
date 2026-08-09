n = int(input("Enter 4 Digit Number : "))

a = n%1000
b = a%100
c = b%10 # last digit number
d = n//1000 # 1st digit


print("First Digit : ",d)
print("Last Digit : ",c)
