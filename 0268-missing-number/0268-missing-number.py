class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total: int = sum(range(len(nums)+1))
        total_list: int = sum(nums)
        return total - total_list
        