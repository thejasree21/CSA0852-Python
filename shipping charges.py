a=int(input("Enter number of items purchased:"))
if a==0:
    print("Shipping charges=",a)
elif a<0:
    print("Negative number")
elif a==1:
    print("Shipping charges=",a*750)
else:
    print("shipping charges =",750+(a-1)*200)
