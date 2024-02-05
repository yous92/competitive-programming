class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str: str = ""
        min_length :int = min(len(word1),len(word2))
        for i in range (min_length):
            merged_str += word1[i]
            merged_str += word2[i]
            
        if (len(word1)>len(word2)):
            merged_str += word1[min_length:]
            
        else:
            merged_str += word2[min_length:]
            
        return merged_str