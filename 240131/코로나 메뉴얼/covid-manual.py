emergency_count = 0

for _ in range(3):
    a, b = map(str, input().split())
    b = int(b)

    if a == 'Y' and b >= 37:
        emergency_count += 1

result_list = []

if emergency_count >= 2:
    result_list.append('E')
else:
    a, b = map(str, input().split())
    b = int(b)

    if a == 'Y' and b >= 37:
        result_list.append('A')
    elif a == 'N' and b >= 37:
        result_list.append('B')
    elif a == 'Y' and b < 37:
        result_list.append('C')
    else:
        result_list.append('D')

for result in result_list:
    print(result)