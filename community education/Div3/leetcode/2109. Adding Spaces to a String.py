class Solution:
    def addSpaces(self, s,spaces):
        res = ""
        f, l = 0, 0
        while l < len(spaces):
            res += s[f:spaces[l]]
            res += " "
            f = spaces[l]
            l += 1
        res += s[f:]
        return res