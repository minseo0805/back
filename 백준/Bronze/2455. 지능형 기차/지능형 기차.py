on = []
people = 0

for i in range(4):
    a, b = map(int, input().split())
    people += b
    people -= a
    on.append(people)

print(max(on))