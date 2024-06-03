n, k = map(int, input().split())

power = 1
for i in range(1, n):
    power *= 2


temp = (power + 1) // 2

if k > temp:
    k = power - k

for i in range(n, 0, -1):
    if k % (2 ** (i - 1)) == 0:
        print(i)
        break
