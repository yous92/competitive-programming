class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer  = [[],[]]
        winners = set([matches[i][0] for i in range(len(matches))])
        losers = [matches[i][1] for i in range(len(matches))]
        losers_dict = Counter(losers)
        for key, value in losers_dict.items():
            if value == 1:
                answer[1].append(key)
        
        for winner in winners:
            if winner not in losers_dict.keys():
                answer[0].append(winner)
        answer[0].sort()
        answer[1].sort()
        return answer