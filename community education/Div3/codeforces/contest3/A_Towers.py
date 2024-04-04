from collections import defaultdict


a = int(input())
b = list(map(int, input().split()))

table = defaultdict(int)

for a in b:
    table[a] += 1

c = d = 0

for k,v in table.items():
    c = max(c, v)
    d += 1

print(c,d)
