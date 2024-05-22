n1, n2 = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


ans = []
l, r = 0, 0
while r < n2:
    while l < n1 and arr1[l] < arr2[r]:
        l += 1
    ans.append(l)
    r += 1

while r < n2:
    ans.append(n1)
    r += 1

print(*ans)