a,b,c = map(int,input().split())

arr = [a,b,c]

if min(arr) == a :
    print('1',end = ' ')
else : 
    print('0', end = ' ')

if a == b == c : 
    print('1', end = ' ')
else : 
    print('0', end = ' ')