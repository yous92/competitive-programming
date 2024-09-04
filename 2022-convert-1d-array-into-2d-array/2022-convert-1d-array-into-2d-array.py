class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = []
        if len(original) != m * n:
            return []
      
        for i in range(m):
            row = original[i * n:(i + 1) * n]
            result.append(row)
        
        return result
       