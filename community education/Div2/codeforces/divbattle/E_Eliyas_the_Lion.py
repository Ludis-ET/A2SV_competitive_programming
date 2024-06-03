s = input().strip()
n = len(s)

adj = [0] * n
for i in range(1, n):
    adj[i] = adj[i - 1] + (s[i] == s[i - 1])

m = int(input())

for _ in range(m):
    l, r = map(int, input().split())
    
    answer = adj[r - 1] - adj[l - 1]
    
    print(answer)
