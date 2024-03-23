n, k = map(int, input().split())
arr = list(map(int, input().split()))

b = a = count = 0
if k > 8 and n == 1:
    print(-1)
else:
    for c in arr:
        if b >= k:
            break
        if c + a <= 8:
            b += c + a
            a = 0 
        else:
            b += 8
            a = (c + a) - 8
        count += 1

    print(count if b >= k and count <= n else -1)
