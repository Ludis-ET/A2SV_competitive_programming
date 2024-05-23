class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for a in costs:
            if coins - a >= 0:
                count += 1
                coins -= a
        return count