n = int(input())

for i in range(1,2*n+1):
    if i%2==0 : 
        for _ in range((i+1)//2):
            print('*',end= ' ')
        print()
    else : 
        for _ in range(n-(i-1)//2,0,-1):
            print('*', end = ' ')
        print()