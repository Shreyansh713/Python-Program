p = int(input("Enter Principal Amount : "))
r = float(input("Enter Rate of Interest : "))
t = int(input("Enter Time/Year : "))

amount = p*(1+(r/100))**t

ci = amount-p

print("Compound Interest : ",ci)