import sys

N, M = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().split()))
sum_numbers = [0 for i in range(N)]

for i in range(N):
    if i == 0:
        sum_numbers[i] = numbers[i]
    else:
        sum_numbers[i] = sum_numbers[i-1] + numbers[i]

for i in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(sum_numbers[j-1])
    else:
        print(sum_numbers[j-1] - sum_numbers[i-2])