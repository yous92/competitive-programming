class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = {(m-1, n-1):1}
        
        def dp(r,c):
            if r == m or c == n or obstacleGrid[r][c]:
                return 0
            
            if (r,c) in memo:
                return memo[(r,c)]
            
            memo[(r,c)] = dp(r+1,c) + dp(r,c+1)
            return memo[(r,c)]
        
        return dp(0,0)
                
                    
                    
                
            
            