n = int(input())
arr = list(map(int, input().split()))

arr.sort()

mx = 0
l = 0
r = 0

while r < n:
    while arr[r] - arr[l] > 5:
        l += 1
    mx = max(mx, r - l + 1)
    r += 1
print(mx)
