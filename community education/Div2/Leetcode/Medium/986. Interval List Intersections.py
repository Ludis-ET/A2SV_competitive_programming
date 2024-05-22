class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstList.sort()
        secondList.sort()
        l = 0
        r = 0
        ans = []
        while l < len(firstList) and r < len(secondList):
            min_l = firstList[l][0]
            max_l = firstList[l][1]
            min_r = secondList[r][0]
            max_r = secondList[r][1]
            0 , 2
            1, 5
            if min_l <= max_r <= max_l or min_r <= max_l <= max_r:
                left = max(min_l,min_r)
                right = min(max_l,max_r)
                ans.append([left,right])
            if max_r <= max_l:
                r += 1
            else:
                l += 1
        return ans
        