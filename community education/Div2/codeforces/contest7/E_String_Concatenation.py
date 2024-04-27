t = int(input())

for _ in range(t):
    n = int(input())
    st = []
    pre = set()
    result = ''
    
    for _ in range(n):
        s = input()
        st.append(s)
        pre.add(s)
    # print(st, pre)
    
    for s in st:
        found = False
        # 'abab'
        for i in range(1, len(s)):
            prefix = s[:i]
            suffix = s[i:]
            # print(prefix, suffix)
            if prefix in pre and suffix in pre:
                found = True
                break
        # print("=======")
        result += "1" if found else "0"
    
    print(result)
