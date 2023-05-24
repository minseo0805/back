n=int(input())
a=0
b=0
for i in range(n):
    if int(input()) == 0:
        a+=1
    else:
        b+=1
        
if a > b:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
    
    