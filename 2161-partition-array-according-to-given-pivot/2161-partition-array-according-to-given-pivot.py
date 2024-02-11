class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
       
        lesser: List[int] = []
        greater: List[int] = []
        equal: List[int] = []
        lesser = [x for x in nums if x<pivot ]
        equal = [x for x in nums if x==pivot]
        greater = [x for x in nums if x>pivot]
        
        return lesser+equal+greater