n = input()
x = list(map(int, input().split()))
ans = []
r = 1
for i in x:
    ans += [r] * int(i)
    r += 1

m = input()
y = list(map(int, input().split()))
for j in y:
    print(ans[int(j)-1])