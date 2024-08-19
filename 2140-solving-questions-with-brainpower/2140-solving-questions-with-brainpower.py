class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        memo = {}
     
        def dp(i):
            if i >= len(questions):
                return 0
            if i in memo:
                return memo[i] 
            
            memo[i] = max(dp(i+1), #skip question
                          questions[i][0] + dp(i+1+questions[i][1])) # solve current question
            
            return memo[i]
        return dp(0)
            
            
                
            
            