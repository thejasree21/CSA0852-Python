a=[]
j=int (input ("Enter the number of elements: "))
print ("Enter the elements of the list: ")
for i in range (0,j):
    x=int (input ())
    a.append (x)
    a.sort ()

m=int (input ("Enter m value: "))
n=int (input ("Enter n value: ") )
sum=a [j-m] +a [n-1]
sub=a [j-m] -a [n-1]
print ("Mth maximum element=",a[j-m])
print ("Nth minimum element=",a[n-1])
print ("Sum=", sum)
print ("Difference=", sub)
