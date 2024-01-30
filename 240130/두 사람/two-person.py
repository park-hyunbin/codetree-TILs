a, b = map(str, input().split())
c, d = map(str, input().split())

a = int(a)
c = int(c)

if (a >= 19 or b == 'M') and (c >= 19 or d == 'M'):
    print('1')
else:
    print('0')