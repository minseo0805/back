import sys
f = sys.stdin.readline

n = f()
a = list(map(int, f().split()))
a2 = list(sorted(set(a)))
#제거한값 리스트로 변환 
dic = {a2[i]:i for i in range(len(a2))}

for i in a:
    print(dic[i], end=' ')