import sys

N = int(sys.stdin.readline())

cnt = 0 # 연산 횟수

cntTable = [0] * ((10**6) + 1)

for i in range(2, len(cntTable), 2):
    cntTable[i] = i // 2 # 2의 배수의 최단연산은 항상 2로 나눈 수이다.

for i in range(3, len(cntTable), 3):
    cntTable[i] = i // 3 # 3의 배수도 마찬가지

for i in range(5, len(cntTable)):
    if cntTable[i] == 0:
        cntTable[i] = i

def search(num):
    global cnt

    if num == 1:
        return
    elif num % 3 == 0:
        cnt += 1
        search(cntTable[num])
        
    elif num % 2 == 0:
        cnt += 1
        search(cntTable[num])
    else:
        cnt += 1
        search(cntTable[num - 1])

search(N)
print(cnt)