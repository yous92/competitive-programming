class Solution:
   
         
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        nums_count:int = Counter(nums)
        occur:int= len(nums)//3
        result:list[int]=[]
        for key, val in nums_count.items():
            if val > occur:
                result.append(key)
        return result
                
        
        
     
        