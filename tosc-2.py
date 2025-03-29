n = int(input())
i = 1
c = 0
while(1):
    d = 1
    while(1):
        d+=1
        if i+d+d>n:
            break
        c+=1
    i+=1
    c+=1
    if i + 2 > n:
        break
print(c)