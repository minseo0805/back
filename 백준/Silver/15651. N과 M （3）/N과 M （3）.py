n, m = map(int, input().split()) 
array = []  # 출력할 수열

def sequence(x): 
    if x == m:   # 수열 m개를 충족할경우 출력
        print(*array) 
        return 
    for i in range(1,n+1): 
           array.append(i) 
           sequence(x+1) # 다음 깊이 탐색 
           array.pop() # 탐사한 내용 제거 
sequence(0)                