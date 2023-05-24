from collections import deque
 
n,k = map(int,input().split())
q = deque()
 
for i in range(1,n+1):
    q.append(i)
    
li = []
print("<",end='')
while q:  
#k-1번째 숫자들을 큐의 마지막으로 넣음 
    for _ in range(k-1):
        q.append(q.popleft())
    print(q.popleft(),end="") 
#k번째 숫자를 출력
    if q:
        print(", ",end="") 
#숫자뒤 , 출력 
print(">")