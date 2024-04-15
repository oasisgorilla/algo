# import sys
# M, N = map(int, sys.stdin.readline().split())

# for i in range(M, N + 1):

#     if i == 1: # 1은 소수가 아니다
#         continue
#     elif i == 2 or i == 3:
#         print(i)
#     else:
#         for j in range(2, int(i**(0.5))+1): # 2 부터 루트i까지 나눴을 때  
#             if i // j > 0 and i % j == 0: # 나눠지면 소수가 아님
#                break
#             else: # 그렇지 않다면 소수
#                 print(i)

#     print("-------")


"""답안"""
m, n = map(int, input().split())

for i in range(m, n + 1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i)