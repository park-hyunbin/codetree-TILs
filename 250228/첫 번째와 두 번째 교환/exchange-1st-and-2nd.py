s = list(input())

first_char = s[0]  
second_char = s[1] 

for i in range(len(s)):
    if s[i] == first_char:
        s[i] = second_char
    elif s[i] == second_char:
        s[i] = first_char

print("".join(s))
