n = int(input())
a = list(map(int, input().split()))

a.sort()  

mex = 1
for num in a:
    if num >= mex:
        mex += 1

print(mex)
