X=int(input())

line=1
while X>line:
    X-=line
    line+=1 #1씩 늘려가면서 빼면서 찾기 
    
if line%2==0:
    a=X
    b=line-X+1 #짝수일때 분자 오름차순 분모 내림차순 
else:
    a=line-X+1 #홀수일때 분자 내림차순 분모 오름차순 
    b=X
    
print(a, '/', b, sep='')