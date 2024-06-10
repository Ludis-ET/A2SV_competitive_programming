n, k = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(zip(a, range(1, len(a) + 1)))
res = []
for x, i in a:
    if x > k:
        break
    k -= x
    res.append(i)
print(len(res))
print(*res)