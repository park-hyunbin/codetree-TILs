given_str = input()
n = int(input())

if n <= len(given_str):
    print(given_str[: -n - 1 : -1])  
else : 
    print(given_str[::-1])  
