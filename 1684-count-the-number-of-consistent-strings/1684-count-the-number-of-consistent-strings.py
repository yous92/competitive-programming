class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_count = set(allowed)
        count = 0
        for word in words:
            if set(word).issubset(allowed_count):   
                count += 1
        return count
            