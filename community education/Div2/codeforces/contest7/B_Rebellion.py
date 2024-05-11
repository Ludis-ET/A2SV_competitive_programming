t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    left = 0
    count = 0
    n -= 1
    while left < n:
        if l[left] == 1 and l[n] == 1:
            n -= 1
        elif l[left] == 1 and l[n] == 0:
            count += 1
            left += 1
            n -= 1
        elif l[left] == 0 and l[n] == 0:
            left += 1
        else:
            left += 1
            n -= 1
    print(count)