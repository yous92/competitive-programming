class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        score = 0
        m = max(nums)
        for i in range(k):
            score += m + i
        return score
          