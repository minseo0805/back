n = int(input()) # 사람 수 
s = list(map(int, input().split())) # 인출 시간
num = 0
s.sort()
for i in range(n):
    for j in range(i + 1):
        num += s[j] # 인출 시간 갱신
print(num)