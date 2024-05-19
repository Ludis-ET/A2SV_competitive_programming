n = int(input())
b = list(map(int, input().split()))

a = [0] * n
max_a = 0

for i in range(n):
    a[i] = b[i] + max_a
    max_a = max(max_a, a[i])
print(*a)
