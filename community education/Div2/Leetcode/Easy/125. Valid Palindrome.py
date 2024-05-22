class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''.join([word for word in s if word.isalnum()]).lower()
        rev = word[-1::-1]
        return word == rev
        