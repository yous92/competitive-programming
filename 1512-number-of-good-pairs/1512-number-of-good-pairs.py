class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs: int = 0
        for j in range (len(nums)):
            i :int = 0
            while i<j:
                if nums[i] == nums[j]:
                    good_pairs +=1
                i+=1
        return good_pairs