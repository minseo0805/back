from collections import deque 
#속도면에서 빠른 collections.deque 사용 
N = int(input()) 
deque = deque([i for i in range(1, N+1)]) 

while(len(deque) >1): 
    deque.popleft()#pop(0)과 같은 기능을 주면서 시간단축 
    move_num = deque.popleft() 
    deque.append(move_num) 
    
print(deque[0])