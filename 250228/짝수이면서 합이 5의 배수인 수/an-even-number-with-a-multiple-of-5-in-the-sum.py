n = input()

def even(n):
    total = sum(int(i) for i in n) 
    return int(n) % 2 == 0 and total % 5 == 0  
if even(n):  
    print("Yes")
else:  
    print("No")
