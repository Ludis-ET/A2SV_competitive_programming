n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

i = 0
x = 0

for _ in range(k):
    while i < n and arr[i] - x == 0:
        i += 1
    
    if i == n:
        print(0)
    else:
        print(arr[i] - x)
        x += arr[i] - x
