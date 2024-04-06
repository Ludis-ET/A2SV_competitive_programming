t = int(input())

for _ in range(t):
    n = int(input()) 
    s = str(input() ) 
    l, r= 0, n - 1
    
    check = True
    
    while l < r:
        if s[l] != s[r]:
            if s[l:r] == s[l:r][::-1]:
                check = True
            else:
                check = False
            break
        l += 1
        r -= 1
    print("yes" if check else "no")
