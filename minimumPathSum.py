# very similar dp solution to the Unique Paths leetcode question
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    val = min(grid[i-1][j], grid[i][j-1])
                    grid[i][j] += val
                
        return grid[-1][-1]
