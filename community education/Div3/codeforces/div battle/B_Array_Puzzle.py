n = int(input())
arr = list(map(int, input().split()))

start = 0
while start < n - 1 and arr[start] < arr[start + 1]:
    start += 1

end = n - 1
while end > 0 and arr[end] > arr[end - 1]:
    end -= 1

if start == n - 1:
    print("yes")
    print("1 1")
elif start < end and arr[:start] + arr[start:end + 1][::-1] + arr[end + 1:] == sorted(arr):
    print("yes")
    print(start + 1, end + 1)
else:
    print("no")
