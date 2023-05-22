n=int(input())
d=0
for i in range(n):
    a,b,c=map(int,input().split())
    
    if a==b==c:
        d=max(d, 10000+a*1000)
    elif a==b:
        d=max(d, 1000+a*100)
    elif a==c:
        d=max(d, 1000+a*100)
    elif b==c:
        d=max(d, 1000+b*100)
    else:
        d=max(d, 100*max(a,b,c))
print(d)    
        
    
