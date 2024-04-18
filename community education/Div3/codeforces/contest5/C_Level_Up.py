s, n = map(int, input().split())

challenges = []
for _ in range(n):
    x, y = map(int, input().split())
    challenges.append((x, y))


challenges.sort()

for x, y in challenges:
    if s > x:
        s += y  
    else:
        print("NO")
        break
else:
    print("YES")
