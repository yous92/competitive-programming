class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = int("".join(map(str, digits)))
        integer += 1
        result = list(map(int,str(integer)))
        return result