x = input('Enter the string: ')
 
w = ""
for i in x:
    w = i + w# i comes first to reverse the string
 
if (x == w):
    print("Yes")
else:
    print("No")
