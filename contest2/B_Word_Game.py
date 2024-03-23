a = int(input())

for _ in range(a):
    u = int(input())
    f = set(input().split())
    s = set(input().split())
    t = set(input().split())
    h = n = m = 0
    for i in f:
        if i in s and i in t:
            continue
        elif i in s or i in t:
            h += 1
        else:
            h += 3
    for i in s:
        if i in f and i in t:
            continue
        elif i in f or i in t:
            n += 1
        else:
            n += 3
    for i in t:
        if i in s and i in f:
            continue
        elif i in s or i in f:
            m += 1
        else:
            m += 3
    print(h, n, m)