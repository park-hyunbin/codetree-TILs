n = int(input())

for i in range(n * 2+1):  
    for j in range(n * 2+1):
        if i % (n - 1) == 0 or j % (n - 1) == 0:  
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()  
