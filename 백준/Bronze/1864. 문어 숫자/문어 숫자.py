dct = {	# 딕셔너리 자료형에 대응값을 넣습니다
       '-':0,
       '\\':1,
       '(':2,
       '@':3,
       '?':4,
       '>':5,
       '&':6,
       '%':7,
       '/':-1
       }

while True: #입력을 무한히 반복합니다
    a = input() #입력값 변수를 받습니다
    if a == '#': #'#'문자를 만나면
        break	#입력이 종료됩니다
    n = len(a)-1	#8진법의 지수는 왼쪽에서 오른쪽으로 가는 경우 (문자의 길이-1)->0까지 지속됩니다
    sum_ = 0 #8진법의 모든 자리수 값을 더한 값이 담기게 됩니다
    for i in a:	#반복문을 실행합니다
        sum_+=dct[i]*(8**n) #i번째 자리수를 8진법으로 변환합니다. +=으로 표시해 기존의 값에 계속해서 더해져 담깁니다
        n-=1 #n = n-1과 동일한 표현입니다. 지수를 1씩 빼줍니다

    print(sum_)