class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        one = [-1]
        for [i, num] in enumerate(nums):
            if num == 1:
                one.append(i)
        one.append(len(nums))

        res = 0
        for i in range(1, len(one) - goal):
            if goal == 0:
                num_of_zero = (one[i] - one[i - 1]) - 1
                res += int((num_of_zero * (num_of_zero + 1)) / 2)
            else:
                num_of_start_zero = (one[i] - one[i - 1]) - 1
                num_of_end_zero = (one[i + goal] - one[i - 1 + goal]) - 1
                res += (num_of_start_zero + 1) * (num_of_end_zero + 1)

        return res