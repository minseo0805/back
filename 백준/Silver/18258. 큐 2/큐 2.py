import sys
from collections import deque # deque로 구현하여 빠른 속도 
n = int(sys.stdin.readline()) #시간초과 때문에 빠른 입력 
q = deque([])
for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == 'push': #정수 x를 큐에 넣음 
        q.append(s[1])
    elif s[0] == 'pop': #큐 가장 앞에 있는 정수빼고 그수 출력 없는경우 -1
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif s[0] == 'size': #큐안에 정수 개수 출력 
        print(len(q))
    elif s[0] == 'empty': #큐가 비어있으면 1, 아니면 0
        if not q:
            print(1)
        else:
            print(0)
    elif s[0] == 'front': #큐 가장 앞에있는 정수 출력 없는경우 -1 
        if not q:
            print(-1)
        else:
            print(q[0])
    elif s[0] == 'back': #큐 가장 뒤에있는 정수 출력 없는경우 -1 
        if not q:
            print(-1)
        else:
            print(q[-1])