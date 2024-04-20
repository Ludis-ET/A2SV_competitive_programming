t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    n = len(arr)
    count = 0
    for i in range(n - k):
        ans = True
        for j in range(1, k + 1):
            if arr[i + j] * (2 ** j) <= arr[i + j - 1] * (2 ** (j - 1)):
                ans = False
                break
        if ans:
            count += 1
    print(count)
