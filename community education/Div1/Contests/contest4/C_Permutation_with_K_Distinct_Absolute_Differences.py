n, k = map(int, input().split())

a =[i for i in range(1, n + 1) if i % k == 0]
b =[i for i in range(1, n + 1) if i % k != 0]


ans = []
l, r = 0, 0 
i = 1
while l < len(a) and r < len(b):
    if i > 0 and i <= k:
        ans.append(b[r])
        r += 1
        i += 1
        continue
    if i > k and i <= 2 * k:
        ans.append(a[l])
        l += 1
        i += 1
        continue
    if i == 2 * k:
        i = 1

if l < len(a):
    ans.extend(a[l:])

if r < len(b):
    ans.extend(b[r:])

print(*ans)

