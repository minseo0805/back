li=[int(input()) for i in range(3)]
if sum(li) == 180:
    if li[0] == li[1] == li[2]:
        print("Equilateral")
    elif li[0] == li[1] or li[1] == li[2] or li[0] == li[2]:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")