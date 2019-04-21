# example: m = 3, n = 2
# 1 1 1
# 1 2 3 <- solution
#
# Imagine grid is an reversed representation of the actual mxn grid;
# grid[0][0] represents the goal and grid[m-1][n-1] represents the start
# each value in the grid represents how many possible paths there are from
# the given point to the goal
#
# as a base case the goal is set to 1 unique way to get to the goal
# we can start by initializing all locations that are directly above (below, on the grid)
# or directly to the left of (to the right of, on the grid) the goal to 1,
# as they only have the path of going straight down or straight right to get to the goal
# then for all other locations, we take the sum of the locations right and below (left and above on the grid)
# to construct the unique paths from the given location to the goal
#
# example step-by-step:
#
# initialize grid
# 0 0 0
# 0 0 0
#
# populate base case
# 1 1 1
# 1 0 0
#
# populate rest of grid with dp
# 1 1 1
# 1 2 0 <- 1 + 1 = 2
#
# 1 1 1
# 1 2 3 < - 2 + 1 = 3

class Solution(object):
    def uniquePaths_optimized(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 1 and n <= 1:
            return 1
        grid = [[0] * n] * m
        grid[0][0] = 1
            
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j-1]
                elif j == 0:
                    grid[i][j] = grid[i-1][j]
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[m-1][n-1]

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 1 and n <= 1:
            return 1
        grid = [[0] * n] * m
        for i in range(m):
            grid[i][0] = 1
        for i in range(n):
            grid[0][i] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[m-1][n-1]
