class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        zer = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zer += 1
            while zer > 1:
                if nums[l] == 0:
                    zer -= 1
                l += 1
            ans = max(ans, r- l)
        return ans 
