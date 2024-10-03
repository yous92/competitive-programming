
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
            common_count = Counter(words[0])
         
            for word in words[1:]:
                new_count = Counter(word)
                for char in list(common_count.keys()):
                    if char in new_count:
                        common_count[char] = min(common_count[char], new_count[char])
                    else:
                        del common_count[char]

            res = []
            for char,num in common_count.items():
                res.extend([char]*num)
            return res
        
                
