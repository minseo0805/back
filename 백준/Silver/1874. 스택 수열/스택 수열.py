n=int(input())
stack=[] #저장할 리스트 
result=[] #표현할 리스트 
count=0 #변수 초기화
X=True 

for i in range(n): 
    num=int(input())
    #count가 num보다 작을떄 stack에 1씩 증가 
    while count < num:
        count +=1
        stack.append(count)
        result.append("+")
    #stack 꼭대기[-1]설정후 pop함수를 통해 수를 빼준후 -추가    
    if stack[-1] ==num:
        stack.pop()
        result.append("-")
    #top이 num로 둘어온 수와 같지않으면 false로 초기화후 break     
    else:
        X=False
        break
        
if X == False:
    print("NO")
else:
    for i in result:
        print(i)
        
        
    
    
    

