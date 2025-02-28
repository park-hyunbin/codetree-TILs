n = int(input()) 

arr = list(map(int,input().split())) 

def is_even(arr): 
    for i in arr:  
        if i % 2 == 0: 
            print(i // 2, end = ' ') 
        else: 
            print(i, end =' ')  

is_even(arr)  
