d = int(input("Enter Day : "))

y = d//365  #400/365 = 1 
a = d%365   #400/365 = 35
m = a//30   #35/30 = 1
rd = a%30   #35/30 = 5


print(y,"Year",m,"month",rd,"days")