n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))#입력한 값 리스트에 추가 
a.sort()#오름차순 정렬 
for i in a:
    print(i)
