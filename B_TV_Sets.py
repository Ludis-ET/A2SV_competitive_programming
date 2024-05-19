
n, m = map(int, input().split())
a = list(map(int, input().split()))

neg = [i for i in a if i < 0]

neg.sort()

mx_tv = min(m, len(neg))
mx_ea = sum(neg[:mx_tv])
print(-mx_ea)
