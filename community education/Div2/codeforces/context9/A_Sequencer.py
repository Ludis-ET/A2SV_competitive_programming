t = int(input().strip())

for _ in range(t):
    x = int(input())
    a = list(map(int, input().split()))
    l, r = 0, len(a) - 1
    ans = []
    while l < r:
        ans.append(a[l])
        ans.append(a[r])
        l += 1
        r -= 1
    if x % 2 != 0:
        ans.append(a[l])
    print(*ans)