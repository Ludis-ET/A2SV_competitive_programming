t = int(input())
for _ in range(t):
    table = {}
    n = str(input())

    for i in range(len(n)):
        table[n[i]] = i + 1

    s = str(input())
    ans = 0
    prev = 0
    for i in s:
        ans += abs(table[i] - prev) if prev > 0 else 0
        prev = table[i]
    print(ans)
