class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            answer[i] = abs(left_sum - (total_sum-left_sum-nums[i]))
            left_sum += nums[i]
        return answer