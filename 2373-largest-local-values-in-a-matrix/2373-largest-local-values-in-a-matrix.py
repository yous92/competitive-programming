class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        result = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
              
                max_value = max([grid[i+x][j+y] for x in range(3) for y in range(3)])
                result[i][j] = max_value

        return result