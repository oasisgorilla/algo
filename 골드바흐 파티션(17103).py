# import sys

# T = int(sys.stdin.readline())

# testCase = []

# for _ in range(T):
#     testCase.append(int(sys.stdin.readline()))

# def primeCheck(num):
#     MAX = 100
#     primeArr = [True for i in range(MAX + 1)]

#     primeArr[1] = False

#     for i in range(2, int(MAX**(0.5)) + 1):
#         if primeArr[i] == True:
#             j = 2
#             while i * j <= MAX:
#                 primeArr[i] = False
#                 j += 2
#     check = primeArr[num]
#     return check

# for case in testCase:
#     #case // 2 한 것 까지의 소수 구하기
#     while True:
#         a = case // 2
#         b = case // 2
#         cnt = 0
#         if primeCheck(a) and primeCheck(b):
#             cnt += 1
#         a += 1
#         b -= 1
#         if b == 0:
#             break

#     print(cnt)

"""답안"""
import sys

# 에라토스테네스의 체
primeNum = [False, False] + [True] * 999999 # 0, 1은 소수가 아니다.

for i in range(2, 1000001):
    if primeNum[i]:
        for j in range(i*2, 1000001, i): # 숫자 i에 대해서
            primeNum[j] = False # i * 2 부터 1000000까지 i의 배수는 소수가 아님

T = int(sys.stdin.readline())

for i in range(T):
    cnt = 0
    N = int(sys.stdin.readline())

    for j in range(2, N // 2 + 1): # 2부터 N//2 + 1까지
        if primeNum[j] and primeNum[N - j]:
            cnt += 1
    print(cnt)

