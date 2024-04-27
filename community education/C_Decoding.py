n = int(input())
s = str(input())
ans = [0] * n
i = 0
while i <= (n // 2 - 1):
    n //= 2
    ans[n] = s[i]
    i += 1

print(ans)