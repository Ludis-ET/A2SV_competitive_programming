t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    f = list(map(int, input().split()))

    du = [f[0] - s[0]]

    for i in range(1, n):
        du.append(f[i] - max(f[i - 1], s[i]))

    print(*du)
