n = int(input())

def print_sum(n):
    if n == 0:
        return 0 
    
    return n + print_sum(n - 1)  

print(print_sum(n))

