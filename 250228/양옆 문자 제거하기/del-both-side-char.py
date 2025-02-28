s = input()

s = s[0:1] + s[2:len(s)-2] + s[-1]
print(s)