t = int(input())

for _ in range(t):
    n, a, p = map(int, input().split())

    s = n*a
    ps = p * (n//2) + (n%2)*a
    print(min(s, ps))