n = input()

def even(n):
    total = 0  
    if int(n) % 2 == 0:  # 짝수인지 확인
        for i in n: 
            total += int(i)  # ✅ 각 자리 숫자의 합 계산
            if total % 5 == 0:  # ✅ 5의 배수인지 확인
                return True  
    return False  # ✅ 모든 조건이 충족되지 않으면 False 반환

if even(n):  
    print("Yes")
else:  
    print("No")
