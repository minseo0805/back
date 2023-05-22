result = ''
for a in range(6, 101):
    for b in range(2, 101):
        for c in range(b + 1, 101):
            for d in range(c + 1, 101):
                if (a * a * a) == (b * b * b) + (c * c * c) + (d * d * d):
                    result += f'Cube = {a}, Triple = ({b},{c},{d})\n'
                if (a * a * a) < (b * b * b) + (c * c * c) + (d * d * d):
                    break
print(result, end='')