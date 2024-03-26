class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        maxLocal = [[0] * (len(grid) - 2) for _ in range(len(grid) - 2)]
        for i in range(len(grid) - 2): 
            for j in range(len(grid) - 2): 
                maxLocal[i][j] = max(grid[ii][jj] for ii in range(i, i+3) for jj in range(j, j+3))
        return maxLocal