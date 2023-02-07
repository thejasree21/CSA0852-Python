n_sum=0
cn=0
p_sum=0
pn=0
print("Enter -1 to exit")
for i in range(100):
    b=int(input("Enter the number:"))
    if b==-1:
        break

    elif b<0:
        n_sum+=b
        cn+=1
        n_avg=n_sum/cn
    else:
        p_sum+=b
        pn+=1
        p_avg=p_sum/pn
print("The average of negative numbers is:",n_avg)
print("The average of positive numbers is:",p_avg)
