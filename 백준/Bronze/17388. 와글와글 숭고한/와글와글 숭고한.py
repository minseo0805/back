a,b,c=map(int,input().split())

if  a+b+c >= 100:
    print("OK")
else:
    if a == min(a,b,c):
        print("Soongsil")
    elif b == min(a,b,c):
        print("Korea")      
    elif c == min(a,b,c):
        print("Hanyang")     