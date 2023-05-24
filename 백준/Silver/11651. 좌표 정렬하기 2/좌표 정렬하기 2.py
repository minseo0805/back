n=int(input())
num=[]
for i in range(n):
    [a,b]=map(int,input().split())
    arr=[b,a]
    num.append(arr)
num=sorted(num) #a,b자리 바꾸고 정렬
for i in range(n):
    print(num[i][1],num[i][0])
    