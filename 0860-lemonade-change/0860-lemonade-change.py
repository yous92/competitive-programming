class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_count = 0 
        ten_count = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                five_count += 1
            elif bills[i] == 10:
                if five_count > 0:
                    ten_count += 1 
                    five_count -= 1
                else:
                    return False
            else:
                if ten_count > 0 and  five_count > 0 :
                        five_count -= 1
                        ten_count -= 1
                elif five_count >= 3:
                    five_count -= 3
                else:
                    return False
        return True 
        