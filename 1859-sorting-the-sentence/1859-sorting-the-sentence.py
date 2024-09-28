class Solution:
    def sortSentence(self, s: str) -> str:
        s_list = s.split(" ")
        rearranged = ['']*len(s_list)
        for word in s_list:
            rearranged[int(word[-1])-1] = word[:-1]
        return " ".join(rearranged)
        