t = int(input().strip())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    l, r = 0, n - 1
    ans = 0
    xx = True
    while l <= r and k > 0:
        if xx:
            a[l] -= min(a[l], k)
            k -= min(a[l], k)
            ans += 1
            if a[l] != 0:
                break
            l += 1
            xx = not xx
        else:
            a[r] -= min(a[r], k)  # Corrected from a[l] to a[r]
            k -= min(a[r], k)
            if a[r] != 0:
                break
            r -= 1
            ans += 1
            xx = not xx
        # print(a, k)
    print(ans)
