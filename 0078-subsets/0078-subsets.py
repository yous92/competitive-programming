class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subset):
          
            results.append(subset[:])

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        results = []
        backtrack(0, [])
        return results