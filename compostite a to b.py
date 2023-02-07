a=int(input("Enter the start range: "))
b=int(input("Enter the end range: "))
if(a<=0 or b<=0):
    print("Enter positive integers")
elif(a==b):
    print("starting and ending range is same")
elif(b<a):
    print("Ending range should be greater than starting range")
else:
    count=0
    for number in range(a+1,b+1):
        count = 0
        for divider in range(2, number//2+1):
            if number%divider == 0:
                count+=1
        if count >= 1:
            print(number)
