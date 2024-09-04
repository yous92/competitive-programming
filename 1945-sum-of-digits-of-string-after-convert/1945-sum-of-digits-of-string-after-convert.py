class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ""
        for c in s:
            num += str(ord(c) - ord('a') + 1)
        
        for _ in range(k):
            result = sum(int(digit) for digit in num)
            num = str(result)

        return result