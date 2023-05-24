a, b = map(int, input().split())
 
str = list(map(int, input().split()))
 
for i in str:
    if i < b:
        print(i, end=" ")