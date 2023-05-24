member_num = int(input()) #회원수
member_list = []

for i in range(member_num): #회원 이름,나이 입력받음 
    member_age, member_name = map(str, input().split())
    member_age = int(member_age)
    member_list.append((member_age, member_name))

#나이 기준 정렬 > 가입순 정렬
member_list.sort(key = lambda member: (member[0]))
#람다 함수 사용 
for member in member_list:
    print(member[0], member[1])