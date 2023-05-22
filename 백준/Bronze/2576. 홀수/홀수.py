li=[]
for i in range(7):
    num=int(input())
    if num % 2 != 0:
        li.append(num)
if li:
    print(sum(li))
    print(min(li))
else:
    print(-1)
    