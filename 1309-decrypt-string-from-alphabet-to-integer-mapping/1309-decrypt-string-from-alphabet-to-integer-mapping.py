class Solution:
    def freqAlphabets(self, s: str) -> str:
        i:int =0 
        res: str = ""
        while i < len(s) : 
            if i+2 < len(s) and s[i+2] == '#':
                res+= chr(int(s[i:i+2])+96) #a = 97
                i+=3
            else:
                res+= chr(int(s[i])+96)
                i+=1
        return res   
        