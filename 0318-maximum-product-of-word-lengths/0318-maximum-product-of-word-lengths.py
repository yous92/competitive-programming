class Solution:
    def maxProduct(self, words: List[str]) -> int:
        state = [0] * len(words)
        ans = 0

        for i in range(len(words)):
            for c in words[i]:
                state[i] |= 1 << (ord(c) - ord('a'))

            for j in range(i):
                if not (state[i] & state[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans
