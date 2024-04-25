# Enter your code here. Read input from STDIN. Print output to STDOUT
e = int(input())
arr1 = set(map(int, input().split()))
f = int(input())
arr2 = set(map(int, input().split()))

print(len(arr1.union(arr2)))
