n, m = map(int, input().split())
tf = list(map(int, input().split()))
pf = list(map(int, input().split()))

cf = [0]
for f in tf:
    cf.append(cf[-1] + f)

l, r =0 ,0

for p in pf:
    while r < n and cf[r] < p:
        r += 1
    t = r
    ans = p - cf[t - 1]
    print(t, ans)
