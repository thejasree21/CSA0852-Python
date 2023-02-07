x=int(input("X = "))
n=int(input("N = "))
print("\n1. Power \n2. Add \n3. Subtract \n4. Multiply \n5. Divide")
while True:
    ch=int(input("Enter the choice: "))
    if ch==1:
        c=x**n
        print("Pow(",x,',',n,')=',c)
    elif ch==2:
        c=x+n
        print("Add(",x,',',n,')=',c)
    elif ch==3:
        c=x-n
        print("Sub(",x,',',n,')=',c)
    elif ch==4:
        c=x*n
        print("Mul(",x,',',n,')=',c)
    elif ch==5:
        if n==0:
            print("Div(",x,',',n,")=Undefined")
        else:
            c=x/n
            print("Div(",x,',',n,')=',c)
    else:
        print("Enter valid choice from 1 to 5")
        break
