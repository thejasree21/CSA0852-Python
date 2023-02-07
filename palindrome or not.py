n=int(input("Enter any number:"))
temp=n
r=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
if(temp==r):
    print("The value is a palindrome")
else:
    print("The number is not palindrome")
