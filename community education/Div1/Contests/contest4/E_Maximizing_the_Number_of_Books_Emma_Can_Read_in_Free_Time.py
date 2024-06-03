n, t = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
total = 0
l = 0

for r in range(n):
    total += a[r]

    while total > t:
        total -= a[l]
        l += 1

    ans = max(ans, r - l + 1)

print(ans)
