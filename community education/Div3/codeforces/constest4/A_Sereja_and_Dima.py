a = int(input())
arr = list(map(int, input().split()))
se, d = 0, 0
n = 0
# print(arr)
f, l = 0, len(arr) - 1
while n < len(arr):
    if n % 2 != 0:
        d += max(arr[f], arr[l])
    else:
        se += max(arr[f], arr[l])
    
    if max(arr[f], arr[l]) == arr[f]:
            f += 1
    else:
            l -= 1
    n += 1


print(se,d)