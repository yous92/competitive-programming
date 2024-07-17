class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        takeOnes = min(numOnes, k)
        k -= takeOnes

      
        takeZeros = min(numZeros, k)
        k -= takeZeros

      
        takeNegOnes = min(numNegOnes, k)

       
        maxSum = takeOnes * 1 + takeZeros * 0 + takeNegOnes * -1
        return maxSum
