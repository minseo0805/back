n= [list(map(int,input().split())) for _ in range(3)]
for i in n:
    if sum(i)==3:
        print("A")
    elif sum(i)==2:
        print("B")
    elif sum(i)==1:
        print("C")
    elif sum(i)==0:
        print("D")
    elif sum(i)==4:
        print("E")