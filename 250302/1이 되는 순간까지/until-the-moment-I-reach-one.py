n = int(input())

def f(n, count=0): 
    if n == 1:  
        return count  
    
    if n % 2 == 0:
        return f(n // 2, count + 1) 
    else:
        return f(n // 3, count + 1) 

print(f(n))
