arr = list(map(int,input().split()))
l = []
for i in arr : 
    if i % 2 == 0 : 
        i = i //2
        l.append(i)
    else : 
        i = i+3 
        l.append(i)

for i in l : 
    if i == 0 :
        break
    print(i, end = ' ')
