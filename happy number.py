num=int(input("Enter a number:"))
def happy_num(n):
    past=set()
    while n!=1:
        n=sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
    return True
print(happy_num(num))
        
