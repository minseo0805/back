n = int(input())
name = 666
count=0
while True:
    if "666" in str(name) : #666이 안에 들어있으면 
        count+=1 #1증가 
    if count == n : #n과 같으면  
        print(name) #출력 
        break
    name+=1 #1씩증가 