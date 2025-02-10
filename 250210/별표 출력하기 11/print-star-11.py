
n = int(input())

if n == 1:
    size = 3
else:
    size = n * 2 + 1


for i in range(n * 2+1):  
    for j in range(n * 2+1):
        if i % (n - 1) == 0 or j % (n - 1) == 0:  
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()  
