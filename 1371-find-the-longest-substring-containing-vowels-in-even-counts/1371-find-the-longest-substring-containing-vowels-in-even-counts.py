class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        mask = 0
        max_length = 0
        first_occurrence = {0: -1}
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}

     
        for i, char in enumerate(s):
         
            if char in vowels:
                mask ^= vowels[char]

          
            if mask in first_occurrence:
                max_length = max(max_length, i - first_occurrence[mask])
            else:
               
                first_occurrence[mask] = i

        return max_length