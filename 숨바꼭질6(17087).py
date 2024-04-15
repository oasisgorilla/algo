"""
수빈이가 동생을 찾기 위해 
1초마다 움직일 수 있는 최대 거리를 구하는 문제이다.
"""
import sys
import math

N, S = map(int, sys.stdin.readline().split())

dist = [0] * N # 동생 위치까지의 거리


bro = list(map(int, sys.stdin.readline().split()))
    
for i in range(N):
    dist[i] = abs(bro[i] - S) # 절대값, 동생 위치까지의 거리

dist.sort()

def GCD(a, b):
    while b!= 0:
        a, b = b, a%b
    
    return a
    
ans = dist[0]
for i in range(len(dist)):
    ans = GCD(ans, dist[i])

print(ans)



