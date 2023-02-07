grade=input("Enter grade of the employee(A/B):")
salary=int(input("Enter employee salary:"))
if(salary<0):
    print("Invalid input")
else:
    if(grade=='A'):
        if(salary<10000):
            bonus=salary*(7/100)
            print("Bonus=",bonus)
            print("Total pay=",salary+bonus)
        else:
            bonus=salary*(5/100)
            print("Bonus=",bonus)
            print("Total pay=",salary+bonus)
    elif(grade=='B'):
        if(salary<10000):
            bonus=salary*(12/100)
            print("Bonus=",bonus)
            print("Total pay=",salary+bonus)
        else:
            bonus=salary*(10/100)
            print("Bonus=",bonus)
            print("Total pay=",salary+bonus)
    else:
        print("Invalid input")
