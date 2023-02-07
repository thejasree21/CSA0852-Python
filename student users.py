tot=int(input("Enter total number of user="))
if(tot==0):
    print("Student users=0")
elif(tot<0):
    print("Invalid input")
else:
    staff=int(input("Enter number of staff user="))
    if(tot==staff):
        print("All the users are staff members")
    elif(tot<staff):
        print("Invalid input")
    else:
        non_staff=staff/3
        print("Student user=",tot-staff-non_staff)
