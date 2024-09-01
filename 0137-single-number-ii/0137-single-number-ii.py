class Solution:
    def singleNumber(self, nums: List[int]) -> int:
     
        result = 0
        for i in range(32):  
            bit_count = 0
            for num in nums:
               
                if (num >> i) & 1:
                    bit_count += 1

            if bit_count % 3 != 0:
                result |= (1 << i)

        if result >= 2**31:  
            result -= 2**32  
        return result
