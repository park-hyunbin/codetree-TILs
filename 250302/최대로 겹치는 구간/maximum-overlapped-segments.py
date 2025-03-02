n = int(input())

segments = [list(map(int, input().split())) for _ in range(n)] 
max_position = max(b for _, b in segments) 
blocks = [0] * (max_position + 1)  

for a, b in segments:
    for i in range(a, b):  
        blocks[i] += 1

max_num = max(blocks)
print(max_num)
