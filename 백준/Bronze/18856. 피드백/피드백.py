N= int(input())
arr = [0 for _ in range(N)]
arr[0] = 1
arr[1] = 2
arr[-1] = 997

for i in range(1,N):
    if arr[i] == 0 :
        arr[i] = arr[i-1] +1
    
print(N)
print(*arr)