class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = [[0] * n for _ in range(n)] 
        for a, b in roads:
            adj[a][b] = adj[b][a] = 1 

        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = sum(adj[i]) + sum(adj[j]) - adj[i][j]  
                max_rank = max(max_rank, rank)

        return max_rank