n, m = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(m)]


# print(c)
c.sort(key=lambda x: x[1], reverse=True)
# print(c)
total = 0
mine = n

for a, b in c:
    match = min(mine, a)
    total += match * b
    mine -= match
    if mine == 0:
        break

print(total)
