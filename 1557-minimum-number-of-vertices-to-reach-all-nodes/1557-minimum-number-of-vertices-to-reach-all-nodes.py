class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n
    
        for edge in edges:
            to_vertex = edge[1]
            in_degree[to_vertex] += 1

        result = []
        for i in range(n):
            if in_degree[i] == 0:
                result.append(i)

        return result