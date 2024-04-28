t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    Set = set()
    ans = ''
    
    for _ in range(n):
        s = input()
        arr.append(s)
        Set.add(s)
    # print(arr, Set)
    
    for s in arr:
        found = False
        # 'abab'
        for i in range(1, len(s)):
            prefix = s[:i]
            suffix = s[i:]
            # print(prefix, suffix)
            if prefix in Set and suffix in Set:
                found = True
                break
            
        # print("=======")
        ans += "1" if found else "0"
    
    print(ans)