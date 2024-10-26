class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        primary_diagonal_sum = 0
        secondary_diagonal_sum = 0

        for i in range(n):
            primary_diagonal_sum += mat[i][i]              
            secondary_diagonal_sum += mat[i][n - 1 - i]    

        total_sum = primary_diagonal_sum + secondary_diagonal_sum

        if n % 2 == 1:
            total_sum -= mat[n // 2][n // 2]

        return total_sum