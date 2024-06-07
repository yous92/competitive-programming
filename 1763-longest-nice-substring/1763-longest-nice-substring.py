class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub: str) -> bool:
      
            return all(c.lower() in sub and c.upper() in sub for c in sub)

        def helper(s: str) -> str:

            if is_nice(s):
                return s


            for i in range(len(s)):
                if s[i].lower() not in s or s[i].upper() not in s:

                    left = helper(s[:i])
                    right = helper(s[i+1:])


                    if len(left) >= len(right):
                        return left
                    else:
                        return right

            return ""

        return helper(s)