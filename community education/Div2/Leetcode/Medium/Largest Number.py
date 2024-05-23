class Solution:
    def largestNumber(self, nums):
        x = [str(x) for x in nums]
        return "".join(sorted(x, key=lambda x: x*10, reverse=True)) if nums[0] != '0'else "0"