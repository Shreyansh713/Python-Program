a,b,c = map(int,input("Enter 3 number : ").split())

if a<b and a<c:
    print(a,"is Smaller")
elif a>b and b<c:
    print(b,"is Smaller")
else:
    print(c,"is Smaller")