t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())
    l, r = 0 , 1
    ans = ""
    while r < n:
        ans += s[l]
        while r < n and s[l] != s[r]:
            r += 1
        l = r + 1
        r = l + 1
    print(ans)
