a = input()
s = a.split('-')
s[0],s[1],s[2] = s[2], s[0], s[1]
result = '.'.join(s)
print(result)