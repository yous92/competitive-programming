class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
    
        dp = [row[:] for row in matrix]

        for i in range(1, n):
            for j in range(n):
                
                min_val = dp[i-1][j]  
                if j > 0:
                    min_val = min(min_val, dp[i-1][j-1])  
                if j < n - 1:
                    min_val = min(min_val, dp[i-1][j+1]) 

                dp[i][j] += min_val

       
        return min(dp[-1])