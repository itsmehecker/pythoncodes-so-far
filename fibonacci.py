l=int(input('Enter the limit'))
a=0
b=1
i=0
while i<l:
    print(a,end=' ')
    c=a+b
    a=b
    b=c
    i+=1