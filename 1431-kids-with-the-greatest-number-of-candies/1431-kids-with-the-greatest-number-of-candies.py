class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        local_max: int
        local_max = max(candies)
        result:list[bool] =[]
        for i in range(len(candies)):
            if candies[i]+extraCandies >= local_max:
                result.append(True)
            else:
                result.append(False)
        return result
            
        
        