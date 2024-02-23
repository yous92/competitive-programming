class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
               
        zeros_counter = nums.count(0)
        result = [nums[i] for i in range(len(nums)) if nums[i]!=0]
        result.extend([0]*zeros_counter)
        return result
        
        
        