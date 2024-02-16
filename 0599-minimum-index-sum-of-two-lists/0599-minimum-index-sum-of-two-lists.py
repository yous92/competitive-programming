class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        sum: int=0
        result:dict[int,str] = {}
        
        for index, element in enumerate(list1):
            if element in list2:
                index2 = list2.index(element)
                sum = index+index2
                if sum in result:
                    result[sum].append(element)
                else:
                     result[sum] = [element]
        min_index = min(result.keys())  
        return result[min_index]