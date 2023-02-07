import math
h=input("Enter number of inputs:")
if h=='2':
    x=int(input("Number1:"))
    y=int(input("Number2:"))
    print("LCM=",math.lcm(x,y))
    print("GCD=",math.gcd(x,y))
elif h=='3':
    x=int(input("Number1:"))
    y=int(input("Number2:"))
    z=int(input("Number3:"))
    print("LCM=",math.lcm(math.lcm(x,y),z))
    print("GCD=",math.gcd(math.gcd(x,y),z))
else:
    print("Invalid input-Enter positive number")
