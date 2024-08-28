class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_xor_y = x ^ y
       
        return bin(x_xor_y).count('1')