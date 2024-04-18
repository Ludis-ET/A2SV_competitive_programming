from collections import defaultdict
n = int(input())
for _ in range(n):
    table = defaultdict(int)
    s = str(input())
    l, r = 0, 0
    ans = ""
    for a in s:
        table[a] += 1
    
    for a, b in table.items():
        if b % 2 != 0:
            ans += a
            
    print(''.join(sorted(ans)))
