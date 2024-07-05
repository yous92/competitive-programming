class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
    
        def get_board_value(index):
           
            quot, rem = divmod(index, n)
            row = n - 1 - quot
            col = rem if quot % 2 == 0 else n - 1 - rem
            return board[row][col]

        visited = set()
        queue = deque([(1, 0)]) 

        while queue:
            curr, moves = queue.popleft()

            for next_square in range(curr + 1, min(curr + 6, n * n) + 1):
                board_value = get_board_value(next_square - 1)
                final_square = board_value if board_value != -1 else next_square

                if final_square == n * n:
                    return moves + 1

                if final_square not in visited:
                    visited.add(final_square)
                    queue.append((final_square, moves + 1))

        return -1
