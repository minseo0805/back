num=int(input()) #반복횟수
for i in range(num):
    h,w,n=map(int,input().split()) #h=건물 층수,w=각 층의 방,n=몇번째 손님
    room=n//h+1 #방 번호
    floor=n%h #층수
    if floor ==0: #층수 =0이면 다른 조건
        room=n//h
        floor=h
    print(f'{floor*100+room}') #문자 변수 같이 출력