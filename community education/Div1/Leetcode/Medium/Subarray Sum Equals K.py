class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        pre = {0 : 1}
        
        for num in nums:
            currSum += num
            diff = currSum - k
            res += pre.get(diff, 0)
            pre[currSum] = 1 + pre.get(currSum, 0)
        
        return res