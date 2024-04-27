t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))






    """
      lr   
    1 0 0 1 1
    0 0 1 1 1
    """
    l, r = 0, n - 1
    count = 0
    while l < r:
        if arr[l] == 1 and arr[r] == 1:
            r -= 1
        elif arr[l] == 1 and arr[r] == 0:
            count += 1
            l += 1
            r -= 1
        elif arr[l] == 0 and arr[r] == 0:
            l += 1
        else:
            l += 1
            r -= 1
    print(count)