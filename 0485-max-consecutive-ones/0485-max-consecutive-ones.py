class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_counter = 0
        max_local = 0
        for element in nums:
            if element == 1:
                max_local +=1
                max_counter = max(max_counter, max_local)
            else:
                max_local = 0
                
        return max_counter