class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        memo = {}
        def dp(start, end):
            if start > end:
                return 0
            
            if (start,end) in memo:
                return memo[(start,end)]
            
            rob_this = nums[start] + dp(start + 2, end)
            skip_this = dp(start + 1, end)

            memo[(start,end)] = max(rob_this, skip_this)

            return memo[(start,end)]

  
        return max(dp(0, len(nums) - 2), dp(1, len(nums) - 1))
