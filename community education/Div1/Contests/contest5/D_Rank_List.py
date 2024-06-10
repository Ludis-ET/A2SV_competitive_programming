n, k=map(int,input().split())
arr = []
for i in range(n):
    l, m = map(int, input().split())
    arr.append([-l,m])

arr.sort()
# print(arr)
print(arr.count(arr[k - 1]))