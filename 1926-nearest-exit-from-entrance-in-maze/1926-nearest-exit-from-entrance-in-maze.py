class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
        m, n = len(maze), len(maze[0])

        queue = deque([(entrance[0], entrance[1], 0)])  

        maze[entrance[0]][entrance[1]] = '+'

        while queue:
            row, col, dist = queue.popleft()

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < m and 0 <= new_col < n and maze[new_row][new_col] == '.':
                    if new_row in {0, m-1} or new_col in {0, n-1}:
                        return dist + 1

                    maze[new_row][new_col] = '+'
                    queue.append((new_row, new_col, dist + 1))

        return -1