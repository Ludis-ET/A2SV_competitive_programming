for _ in range(int(input())):
	n = int(input())
	l = list(map(int,input().split()))
	c = 0
	ans='YES'
	for i in range(n-1):
		if l[i]<l[i+1]:
			c=1
		elif l[i]>l[i+1] and c==1:
			ans='NO'
			break
	print(ans)
