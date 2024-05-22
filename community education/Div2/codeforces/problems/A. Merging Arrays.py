a, b = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1.append(float("inf"))
arr2.append(float("inf"))
ans = []
l, r = 0, 0
# print(arr1, arr2)
while l <= a and r <= b:
    if arr1[l] <= arr2[r]:
        ans.append(arr1[l])
        l += 1
    else:
        ans.append(arr2[r])
        r += 1
ans.pop()
print(*ans)