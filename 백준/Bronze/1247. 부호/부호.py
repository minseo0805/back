import sys
input=sys.stdin.readline

for i in range(3):
    a=int(input())
    num=[int(input()) for i in range(a)]
    
    if sum(num)==0:
        print(0)
    elif sum(num) > 0:
        print("+")
    else:
        print("-")