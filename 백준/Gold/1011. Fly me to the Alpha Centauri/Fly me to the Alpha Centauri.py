a = int(input()) #테스트 케이스 

for i in range(a):
    x, y = map(int,input().split()) #x현재 위치 y 목표 위치
    distance = y - x #가야하는 거리 
    count = 0  # 이동 횟수
    move = 1  # count별 빈도수
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance : #이동한 거리가 가야하는 거리에 도달할떄 까지 반복 
        count += 1 #while문 반복 할떄마다 +1
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0 :  # count가 2의 배수일 때, 
            move += 1 #빈도수 +1
    print(count)