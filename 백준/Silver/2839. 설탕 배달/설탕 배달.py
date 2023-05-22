sugar = int(input()) 

a = 0
while sugar >= 0 : #sugar가 0이 될때까지 반복 
    if sugar % 5 == 0 :  # 5의 배수이면
        a+= (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(a)
        break
    sugar -= 3  
    a += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)