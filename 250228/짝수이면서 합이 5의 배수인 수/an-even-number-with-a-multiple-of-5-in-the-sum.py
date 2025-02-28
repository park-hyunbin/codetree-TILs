n = input()

def even(n):
    total = 0  
    if int(n) % 2 == 0: 
        for i in n: 
            total += int(i) 
                if total % 5 == 0: 
                    return True  
    return False  
if even(n):  
    print("Yes")
else:  
    print("No")
