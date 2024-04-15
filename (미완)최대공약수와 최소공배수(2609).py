import sys

A, B = map(int, sys.stdin.readline().split())

if A > B: #A에 작은 수가 오도록
    A, B = B, A

max_div = 0 # 최대 공약수
min_mul = A * B # 최소 공배수

#최대 공약수
# 2 2 2 3
# 2 3 3

for i in range(2, A + 1): # 2부터 A까지, A가 최대공약수인 경우도 있음 !범위 수정
    if A // i > 0 and B // i > 0:
        if A % i == 0 and B % i == 0:
            max_div = i

print(max_div)

# 최소 공배수

for i in range(2, A + 1): # 최소공배수는 무조건 A * B보다 같거나 작다
    for j in range(i, B + 1):
        if A * j > B * i:
            continue
        
        if B * i == A * j:
            min_mul = B * i
            break
print(min_mul)