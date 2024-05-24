class Solution:
    def balancedString(self, s):
        n, left, min_len, dict1 = len(s), 0, len(s), Counter(s)

        for right in range(n):
            dict1[s[right]] -= 1 

            while left < n and 4*max(dict1.values()) <= n:
                min_len = min(min_len,right-left+1)
                dict1[s[left]] += 1 
                left += 1 

        return min_len 