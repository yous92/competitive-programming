class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        indexed_tasks = [(enqueue, process, i) for i, (enqueue, process) in enumerate(tasks)]

  
        indexed_tasks.sort()

        result = []
        min_heap = []
        time = 0
        i = 0
        n = len(tasks)

        while len(result) < n:
         
            while i < n and indexed_tasks[i][0] <= time:
                heapq.heappush(min_heap, (indexed_tasks[i][1], indexed_tasks[i][2]))
                i += 1

            if min_heap:
               
                process_time, index = heapq.heappop(min_heap)
                time += process_time
                result.append(index)
            else:
               
                time = indexed_tasks[i][0]

        return result