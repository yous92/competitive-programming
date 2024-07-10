import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = []
        for pile in piles:
            heapq.heappush(max_heap, -pile)
      
        for _ in range(k):
            largest_pile = -heapq.heappop(max_heap)
            reduced_pile = (largest_pile + 1) // 2  
            heapq.heappush(max_heap, -reduced_pile)
      
        return -sum(max_heap)
