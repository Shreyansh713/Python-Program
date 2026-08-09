p = int(input("Enter Price : "))
d = int(input("Enter Discount : "))

discount = p*d/100
net = p - discount

print("Net Price :",net)