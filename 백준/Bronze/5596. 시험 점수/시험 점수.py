a,b,c,d=map(int,input().split())
e,f,g,h=map(int,input().split())
li1=[a,b,c,d]
li2=[e,f,g,h]
if sum(li1) >= sum(li2):
    print(sum(li1))
else:
    print(sum(li2))