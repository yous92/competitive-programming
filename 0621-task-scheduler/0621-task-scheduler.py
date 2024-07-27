from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        print(freq)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        time = 0
        q = deque()
      
        while max_heap or q:
            time+=1
            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1
                if count != 0 :
                    q.append([count, time+n])

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
                
        return time
            
            
            
        
        