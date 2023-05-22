n = int(input())
x = 0
for i in range(1, n+1):         # 1부터 n까지
    a = list(map(int, str(i)))  # 각 자리 수 분해
    b = i + sum(a)              # 분해합을 구함
    if(b == n):                 # 분해합이 n과 같다면
        x = i                   # x = i, 종료
        break

print(x)