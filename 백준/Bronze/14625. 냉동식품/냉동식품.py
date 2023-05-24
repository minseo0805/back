H, M = map(int, input().split())
end_H, end_M = map(int, input().split())
N = int(input())

limit = end_H * 60 + end_M - (H * 60 + M)
result = 0
for _ in range(limit + 1):
    if N in [H // 10, H % 10, M // 10, M % 10]:
        result += 1
    M += 1
    if M == 60:
        H += 1
        M = 0
print(result)