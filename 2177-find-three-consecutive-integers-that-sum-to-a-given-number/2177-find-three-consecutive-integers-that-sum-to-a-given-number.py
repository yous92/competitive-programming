class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        result: list[int] = []
        if num % 3 == 0:
            x=num // 3
            result.append(x-1)
            result.append(x)
            result.append(x+1)
        return result
        