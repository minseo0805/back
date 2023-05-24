import sys
N, M = map(int, input().split())

#원래 매트릭스 받기
matrix = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

#열별로 sum한 매트릭스 따로 만들어주기 
for i in range(N):
    for j in range(N):
        if j == 0:
            pass
        else:
            matrix[i][j] += matrix[i][j-1] 

#행별 합 출력
for i in range(M):
    i, j, x, y = map(int, sys.stdin.readline().split())
    answer = 0
    for k in range(i-1, x):
        if j != 1:
            answer -= matrix[k][j-2]
        answer += matrix[k][y-1]
    print(answer)