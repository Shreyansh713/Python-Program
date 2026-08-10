a = input("Enter value/word/symbol :")

if 'A'<= a <= 'Z': 
    print("Character in Uppercase")
elif 'a'<=a<='z':
    print("Character in Lowercase")
elif '0'<=a<='9':
    print("It is a Number")
else:
    print("Symbol")