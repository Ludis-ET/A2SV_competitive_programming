a = int(input())
for _ in range(a):
    b = int(input())
    c = list(map(int, input().split()))
    c.sort(reverse = True)
    e = 0
    while len(c) > 1:
        l = c.pop()
        e = max(e, l)
        for d in range(len(c)):
            c[d] -= l
    e = max(e , c[0])
    print(e)
            
    