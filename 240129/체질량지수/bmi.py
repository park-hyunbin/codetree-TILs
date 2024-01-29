a, b = map(int, input().split())
bmi = b // (0.01 * a * 0.01 * a)

if bmi >= 25: 
    print(int(bmi))
    print("Obesity")
else: 
    print(int(bmi))