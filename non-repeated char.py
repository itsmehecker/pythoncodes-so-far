name = input('ENTER TO GET THE NON-REPEATED CHARACTERS IN A STRING') #little messy but will get the job done
refined = name
length = len(name)
n = 0

while n < length:
    if n < length - 1:
        if refined[n] == refined[n + 1]:
            n += 1
        else:
            print(refined[n])
    else:
        print(refined[n])
    n += 1
