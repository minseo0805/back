for _ in range(int(input())):
    N = int(input())
    li = sorted(map(int, input().split()))
    print(li[0], li[-1])
