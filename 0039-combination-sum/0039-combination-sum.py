class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, combination, remaining_target):
            if remaining_target == 0:
                results.append(list(combination))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining_target:
                    break
                combination.append(candidates[i])
                backtrack(i, combination, remaining_target - candidates[i])
                combination.pop()

        candidates.sort()
        results = []
        backtrack(0, [], target)
        return results