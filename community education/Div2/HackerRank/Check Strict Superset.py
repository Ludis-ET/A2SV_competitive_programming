# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int, input().split()))
n = int(input())
ans = True
for _ in range(n):
    s = set(map(int, input().split()))
    if len(s) >= len(a):
        ans = False
        break
    for i in s:
        if i not in a:
            ans = False
            break
    if not ans: break
print(ans)