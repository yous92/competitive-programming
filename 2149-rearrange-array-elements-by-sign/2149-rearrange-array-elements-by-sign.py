class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        result:list[int]=[0]*len(nums)
        index_pos:int=0
        index_neg:int=1
        
        for element in nums:
            if element > 0 :
                result[index_pos] = element
                index_pos+=2
                
            else:
                result[index_neg] = element
                index_neg+=2
             
        
        return result
            
        