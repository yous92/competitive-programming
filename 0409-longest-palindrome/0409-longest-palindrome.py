class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        odd_found = False
        length = 0
        
        for count in counter.values():
            if count % 2 == 0:
                length += count
            else:
                length += count -1 
                odd_found = True
        if odd_found:
            length += 1
            
        return length
        
        
        