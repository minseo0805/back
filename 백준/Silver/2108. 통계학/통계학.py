import sys
 
N = int(input())
a = []
for _ in range(N):
    a.append(int(sys.stdin.readline()))
a.sort()
 
def average(a):
    return round(sum(a)/len(a))
 
def center(a):
    return a[len(a)//2]
 
def freq(a):
    import collections
    tmp = collections.Counter(a).most_common()
 
    if len(tmp) > 1:
        if tmp[0][1] == tmp[1][1]:
            return tmp[1][0]
        else:
            return tmp[0][0]
    else:
        return tmp[0][0]
 
def range(a):
    return a[len(a)-1] - a[0]
 
print(average(a))
print(center(a))
print(freq(a))
print(range(a))
