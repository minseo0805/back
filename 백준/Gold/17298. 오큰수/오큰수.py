N = int(input()) 
numbers = list(map(int, input().split())) 

stack = [];answer =[-1] * N 

# solution 
for i in range(N): 
    while stack and numbers[stack[-1]] < numbers[i]: 
        answer[stack.pop()] = numbers[i] 
    stack.append(i) 

print(*answer)

#▶ 알고리즘 풀이 (스택)
#단순히 오른쪽에 있는 가장 큰 값이 아니라 해당 수열 오른쪽에 있으면 
#더 큰 수들 중 가장 왼쪽에 있는 값을 요구하므로 스택 활용 결정
#총 N개의 값을 가진 answer을 완성해야 하므로 N번 for문 형성
#stack의 LIFO 성질 (마지막에 넣은게 가장 먼저 나옴) 활용
#조건에 맞지 않을 경우, answer 값은 -1 조건에 맞는다면, answer에 오큰수 대입
#for문 자체를 index로 잡았기에 스택은 index로 활용


