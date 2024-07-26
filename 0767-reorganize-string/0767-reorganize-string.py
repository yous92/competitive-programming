import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
    
        # Create a max heap based on the frequency of characters
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)

        prev_count, prev_char = 0, ''
        result = []

        while max_heap:
            count, char = heapq.heappop(max_heap)
            # Append the current character to the result
            result.append(char)
            # If the previous character count is not zero, push it back to the heap
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))

            # Update the previous character and count (decrement count by 1)
            prev_count, prev_char = count + 1, char

        result = ''.join(result)

        # If the result length is equal to the input string length, return the result
        if len(result) == len(s):
            return result
        else:
            return ""