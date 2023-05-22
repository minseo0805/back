# 1부터 10000까지 숫자 저장 
num_set = set(range(1, 10001)) 
# 셀프 넘버가 아닌 수를 저장 
not_self_num= set() 

for i in range(1, 10001): 
    for j in str(i): #숫자를 문자열로 변환하여 102이면 1, 0, 2로 접근 
        i += int(j) # d(i) = i + j1 + j2 + j3 + .. = 102 + 1 + 0 + 2 
    not_self_num.add(i) # 셀프 넘버가 아닌 수 저장 
# 셀프 넘버만 있는 set = 전체 수 set - 셀프 넘버가 아닌 수 set 
self_num = num_set - not_self_num 
# 오름차순으로 정렬 후 출력 
for i in sorted(self_num): print(i)
