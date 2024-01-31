result_list = []

for _ in range(3) :
    a,b = map(str,input().split())
    b = int(b)

    list = []
    

    if a == 'Y' and b >= 37 : 
        list.append('A')
    elif a == 'N' and b >= 37 :
        list.append('B')
    elif a == 'Y' and b <37 : 
        list.append('C')
    else : 
        list.append('D')

    result_list.extend(list)

if result_list.count('A') >= 2:
    print('E') 
else : 
    print('N')