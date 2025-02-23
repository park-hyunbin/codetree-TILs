str1 = input()
str2 = input()
str3 = input()

a=min(len(str1),len(str2),len(str3))
b=max(len(str1),len(str2),len(str3))

print(b-a)