from collections import defaultdict

t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int,input().split()))
	d = defaultdict(int)
	for i in a:
		d[i] += 1
		
	v = list(d.values())
	if 1 in v:
		print(-1)
	else:
		tmp = 0
		for k in d:
			print(tmp + d[k], end=' ')
			for j in range(tmp + 1,tmp + d[k]):
				print(j,end=' ')
			tmp += d[k]