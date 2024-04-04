class Solution:
    def reverseVowels(self, s):
        l, r = 0, len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u'}
        s = list(s)
        while l < r:
            a, b = s[l], s[r]
            if a.lower() in vowels and b.lower() in vowels:
                s[l], s[r] = b, a
                l += 1
                r -= 1
            elif a.lower() in vowels:
                r -= 1
            else:
                l += 1
        return ''.join(s)
