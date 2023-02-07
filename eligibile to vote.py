try:
    n=int(input("Enter your age:"))
    if(n<=0):
        print("Invalid input-Enter positive integer")
    elif(n>=18):
        print("Eligible to vote")
    else:
        print("You are allowed to vote after",18-n,"years")
except ValueError:
    print("Invalid input")
