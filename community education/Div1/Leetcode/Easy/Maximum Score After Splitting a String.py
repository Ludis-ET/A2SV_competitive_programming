class Solution:
    def maxScore(self, s: str) -> int:
        a = s.count('1')
        z, ans = 0, 0
        for i in range(len(s)-1):
            if s[i] == '0':
                z += 1
            elif s[i] == '1':
                a -= 1
            ans = max(ans, z + a)
        return ans