str_1 = input().split()

if len(str_1[0])>len(str_1[1]):
    print(str_1[0], len(str_1[0]))
elif len(str_1[0])<len(str_1[1]): 
    print(str_1[1],len(str_1[1]))
else : 
    print('same')
