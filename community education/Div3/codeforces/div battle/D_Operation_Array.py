t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()

    instance = sum(arr[:n - k])

    ans = sum(arr[:n - k])
    l, r = 0, n - k
    while r < n:
        instance += arr[r]
        instance -= arr[l]
        l += 1
        instance -= arr[l]
        l += 1
        r += 1
        ans = max(instance, ans)
            
    print(ans)
