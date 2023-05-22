a = int(input())
b = list(map(int, input().split()))
c = max(b)
d = 0
 
for i in range(0, a):
    b[i] = b[i]/c*100
    d = d + b[i]
 
d = d/a
print(d)