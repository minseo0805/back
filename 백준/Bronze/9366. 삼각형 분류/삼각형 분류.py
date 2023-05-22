t = int(input())
for i in range(t):
    a, b, c = list(map(int, input().split()))
    nums = sorted([a, b, c])   
    if nums[2] < sum(nums[:2]):
        if a == b == c:
            print('Case #' + str(i + 1) + ': equilateral')
        elif a == b or b == c or c == a:
            print('Case #' + str(i + 1) + ': isosceles')
        elif a != b or b != c or c != a:
            print('Case #' + str(i + 1) + ': scalene')
    else:
        print('Case #' + str(i + 1) + ': invalid!')