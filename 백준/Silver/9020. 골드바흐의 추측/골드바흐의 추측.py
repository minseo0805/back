import sys
input = sys.stdin.readline

# 0 ~ 10000 사이 값들 소수 여부 리스트 만들기
maximum = 10001
prime = [True] * maximum
for i in range(2, maximum):
  if prime[i] == True: # 기준값이 소수인 경우에만 작업 
    for j in range(2*i, maximum, i):
      prime[j] = False # 기준값의 배수들은 모두 소수가 아님 (기준값을 약수로 가지고 있기 때문)


# 입력값에 대한 골드바흐 파티션 출력하기
T = int(input())
for _ in range(T):
  x = int(input()) // 2 # 골드바흐 파티션이 여러가지인 경우라면 두 소수의 차이가 가장 작은 것을 출력하므로
                         #입력값의 중앙(절반)을 기준으로 양옆으로 1씩 옮기며 두값이 소수인지 판별하기
  i = 0
  while True:
    if prime[x-i] == True and prime[x+i] == True:
      print(f'{x-i} {x+i}')
      break
    i += 1