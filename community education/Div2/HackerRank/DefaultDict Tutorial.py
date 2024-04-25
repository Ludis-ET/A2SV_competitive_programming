from collections import defaultdict

a, b = map(int, input().split())
table = defaultdict(list)
for i in range(a):
    inp = str(input())
    table[inp].append(i + 1)
    
for _ in range(b):
    inp = str(input())
    if len(table[inp]) > 0:
        print(*table[inp])
    else:
        print(-1)