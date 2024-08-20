class Solution:
    def rob(self, nums: List[int]) -> int:
        # state -> index
        # recursion pick no pick -> pick i and goto i + 2,, no pick go i + 1
        # base case -> index > lenght of nums
        memo = {}
        def dp(i, last):
            if i > last:
                return 0
            if (i, last) in memo:
                return memo[(i, last)]
            memo[i, last] = max(nums[i] + dp(i + 2, last), dp(i + 1, last))
            return memo[(i, last)]
        N = len(nums)
        if N == 1:
            return nums[0]
        return max(dp(0, N - 2), dp(1, N - 1))