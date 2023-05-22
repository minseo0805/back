T = int(input()) 
for i in range(T) :
    #빈칸 입력
    temp = input() 
    N = int(input())
    total = 0   
    # 사탕 갯수 합치기
    for j in range(N) :
        total += int(input())
        
    if total % N == 0 : 
        print("YES")
    else : 
        print("NO")