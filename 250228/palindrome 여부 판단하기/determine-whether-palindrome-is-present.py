s = input()

def is_palindrome(s): 
    if "".join(reversed(s)) == s:
        print("Yes") 
    else: 
        print("No")  

is_palindrome(s)  
