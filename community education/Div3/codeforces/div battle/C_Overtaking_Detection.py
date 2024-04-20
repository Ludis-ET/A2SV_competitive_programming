n = int(input())
enter = list(map(int, input().split()))
exited = list(map(int, input().split()))

table = {}
for i in range(n):
    table[exited[i]] = i

ans = 0
Max = -1
for car in enter:
    if table[car] > Max:
        Max = table[car]
    else:
        ans += 1

print(ans)
