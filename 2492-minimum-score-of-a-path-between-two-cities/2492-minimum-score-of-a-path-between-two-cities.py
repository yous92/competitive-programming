class Solution:
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [1] * n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])  
            return self.parent[x]

        def union(self, x, y):
            rootX = self.find(x)
            rootY = self.find(y)

            if rootX != rootY:
                
                if self.rank[rootX] > self.rank[rootY]:
                    self.parent[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.parent[rootX] = rootY
                else:
                    self.parent[rootY] = rootX
                    self.rank[rootX] += 1

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = self.UnionFind(n)
        result = float("inf")

        for a, b, _ in roads:
            uf.union(a - 1, b - 1)

        for a,b,distance in roads:
            if uf.find(a-1) == uf.find(0):
                result = min(result, distance)
        
        return result
        
    
