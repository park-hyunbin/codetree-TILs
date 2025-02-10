n = int(input())

for i in range(1, 2 * n+1):  
    if i % 2 == 1:  
        count = (i // 2) + 1
    else:  
        count = n - ((i-1) // 2)
    
    for j in range(count):
        print('*', end=' ')
    print()  
