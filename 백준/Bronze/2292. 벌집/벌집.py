n = int(input())

numbers = 1  # 벌집의 개수, 1부터 시작
cnt = 1
while n > numbers :
    numbers += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복문을 반복하는 횟수
print(cnt)