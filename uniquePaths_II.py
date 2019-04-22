class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # use existing obstacleGrid for dp
        obstacleGrid[0][0] = 1
        # if previous grid value is 1 and current grid value does not have obstacle, set to 1 path else 0 paths available
        for i in range(1, m):
            if obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1:
                obstacleGrid[i][0] = 1
            else:
                obstacleGrid[i][0] = 0
        for j in range(1, n):
            if obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1:
                obstacleGrid[0][j] = 1
            else:
                obstacleGrid[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
                else:
                    # if it's not already 0, it's an obstacle so no paths available
                    obstacleGrid[i][j] = 0
                    
        return obstacleGrid[m-1][n-1]
        