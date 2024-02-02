class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x: int =0
        supported_operations = {
            "++X" : 1,
            "X++" : 1,
            "--X" : -1,
            "X--": -1
        }
        x = 0
        try:
            for operation in operations:
                x += supported_operations[operation]
            return x
        except KeyError:
             print('Operation not supported')   
    
        