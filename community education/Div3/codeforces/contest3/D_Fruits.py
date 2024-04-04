a, b = map(int,input().split())
c = list(map(int, input().split()))
d = set()
z = []
for _ in range(b):
    f = str(input())
    d.add(f)
    z.append(f)
c.sort()
b = len(d)
mi = sum(c[:b])
ma = sum(c[-(b):])
nxt = len(z) - len(d) 
for a in range(1, nxt + 1):
    mi += c[0]
    ma += c[-1]
print(mi, ma)