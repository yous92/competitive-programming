class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            y = - heapq.heappop(max_heap)
            x = - heapq.heappop(max_heap)
            
            if x != y:
                new_weight = y-x
                if new_weight > 0:
                    heapq.heappush(max_heap,-new_weight)
                
        return -max_heap[0] if max_heap else 0