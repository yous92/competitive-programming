class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        visited = set('0000')
        queue = deque([('0000', 0)])  # (current state, number of moves)

        while queue:
            state, moves = queue.popleft()

            if state == target:
                return moves

            if state in dead:
                continue

            for i in range(4):
                for move in (-1, 1):
                    next_state = list(state)
                    next_state[i] = str((int(state[i]) + move) % 10)
                    next_state = ''.join(next_state)

                    if next_state not in visited and next_state not in dead:
                        visited.add(next_state)
                        queue.append((next_state, moves + 1))

        return -1
