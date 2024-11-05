class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        results = []

        
        for i in range(len(expression)):
            if expression[i] in '+-*':
               
                left = expression[:i]
                right = expression[i+1:]

               
                left_results = self.diffWaysToCompute(left)
                right_results = self.diffWaysToCompute(right)

                
                for left_result in left_results:
                    for right_result in right_results:
                        if expression[i] == '+':
                            results.append(left_result + right_result)
                        elif expression[i] == '-':
                            results.append(left_result - right_result)
                        elif expression[i] == '*':
                            results.append(left_result * right_result)

        return results