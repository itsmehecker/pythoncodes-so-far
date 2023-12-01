l = ['hello',23,69,29.1]
sum=0
for i in l:
    if isinstance(i, (int,float)):#checks if i is int or float(real no.)
        sum=sum+i
print(sum)#prints the sum of all the numeric characters in the list