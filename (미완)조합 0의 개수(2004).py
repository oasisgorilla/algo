import sys

n, m = map(int, sys.stdin.readline().split())

n_fac = n

for i in range(m):
    n_fac *= n - 1
    n -= 1

m_fac = m - 1

for i in range(n - m):
    m_fac *= m - 1
    m -= 1
    
comb = str(n_fac // m_fac)
print(comb)

ans = 0 # 답이 될 변수

# 0이 몇개인지 판별하는 식
for i in comb:
    if i == "0":
        ans += 1

print(ans)