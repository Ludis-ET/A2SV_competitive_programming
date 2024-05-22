class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table1 = defaultdict(int)
        table2 = defaultdict(int)
        for a in nums1: table1[a] += 1
        for a in nums2: table2[a] += 1
        ans = []
        for a in table1:
            if a in table2:
                count = min(table1[a], table2[a])
                ans.extend([a] * count)
        return ans
