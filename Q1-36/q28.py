n = int(input("Enter Three Digit number : "))
a = n%100
b = a%10
c = a//10
d = n//100


print("Reverse of Three Digit Number : ",b,c,d,sep="")