class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reversed_graph = defaultdict(list)
        in_degree = [0] * n

        
        for u in range(n):
            for v in graph[u]:
                reversed_graph[v].append(u)
                in_degree[u] += 1

       
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        safe_nodes = []

     
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for neighbor in reversed_graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        
        return sorted(safe_nodes)