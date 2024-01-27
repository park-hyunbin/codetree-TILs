year = input()
s= year.split('.')
s[0],s[1],s[2] = s[1],s[2],s[0]
result = ('-').join(s)
print(result)