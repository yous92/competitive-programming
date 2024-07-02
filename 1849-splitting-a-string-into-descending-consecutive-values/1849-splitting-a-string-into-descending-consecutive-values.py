class Solution:
    def splitString(self, s: str) -> bool:
        def can_split_from_index(index, prev_value):
            if index == len(s):
                return True
            for i in range(index, len(s)):
                current_value = int(s[index:i+1])
                if current_value + 1 == prev_value:
                    if can_split_from_index(i + 1, current_value):
                        return True
            return False

        for i in range(len(s) - 1):
            current_value = int(s[:i+1])
            if can_split_from_index(i + 1, current_value):
                return True

        return False