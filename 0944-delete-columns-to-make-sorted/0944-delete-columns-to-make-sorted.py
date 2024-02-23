class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        counter = 0
        columns = [[row[i] for row in strs] for i in range(len(strs[0]))]
        for col in columns:
            for i in range(len(col)-1):
                if col[i] > col[i+1]:
                    counter+=1
                    break
        return counter           
                    