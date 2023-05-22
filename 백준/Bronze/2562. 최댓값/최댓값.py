num = []
for i in range(0,9):
    a=int(input())
    num.append(a)
maxn = max(num)
print(maxn)
print(num.index(maxn)+1)