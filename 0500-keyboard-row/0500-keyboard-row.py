class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result: list[str] = []
        for word in words:
            word_set = set(word.lower())
            if word_set <= set("qwertyuiop") or word_set <= set("asdfghjkl") or word_set <= set("zxcvbnm"):   
                result.append(word)
                
        return result