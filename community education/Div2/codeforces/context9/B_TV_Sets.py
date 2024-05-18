
n, m = map(int, input().split())
a = list(map(int, input().split()))

neg = [i for i in a if i < 0]

neg.sort()

mx_tv = min(m, len(neg))
mx_ea = sum(neg[:mx_tv])
print(-mx_ea)


n,m= list(map(int,input().split()))
ls= list(map(int,input().split()))

neg = [i for i in ls if i < 0]
neg.sort()
i=0
ans=0
while ls[i]<0 and m>0 and i<n:
    ans+=abs(ls[i])
    i+=1
    m-=1
print(ans)