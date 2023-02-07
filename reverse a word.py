def reverse(s):
    str=" "
    for i in s:
        str=i+str
    return str
s=input("Enter any string:")
print("Original String:",s)
print("Reverse String:",reverse(s))
