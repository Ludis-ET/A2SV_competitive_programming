class Solution:
    def isValid(self, s: str) -> bool:
        table = {'(' : ')' , "[" : "]" , "{" : "}"}
        n = 0
        while n < len(s) and len(s) > 1:
            if table[s[n]] != s[n + 1]:
                return False
            n += 2
        return True