n = int(input())
for i in range(n):
    fi = []
    ab = list(map(int, input().split()))
    for j in range(4):
        fi.append(ab[4 + j] + ab[j])
    if fi[0] < 1:
        fi[0] = 1
    if fi[1] < 1:
        fi[1] = 1
    if fi[2] < 0:
        fi[2] = 0
    print(fi[0] * 1 + fi[1] * 5 + fi[2] * 2 + fi[3] * 2)