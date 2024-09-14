class Solution:
    # Time Complexity:\U0001d442(\U0001d45blog\U0001d45b)O(nlogn), where \U0001d45b is the number of stones.
    # Space Complexity: \U0001d442(\U0001d45b)
    def removeStones(self, stones: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self):
                self.parent = {}
                self.rank = {}

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])  # Path compression
                return self.parent[x]

            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)

                if rootX != rootY:
                    # Union by rank
                    if self.rank[rootX] > self.rank[rootY]:
                        self.parent[rootY] = rootX
                    elif self.rank[rootX] < self.rank[rootY]:
                        self.parent[rootX] = rootY
                    else:
                        self.parent[rootY] = rootX
                        self.rank[rootX] += 1

            def add(self, x):
                if x not in self.parent:
                        self.parent[x] = x
                        self.rank[x] = 0

       
        uf = UnionFind()

        for x, y in stones:
                uf.add(x)
                uf.add(~y)  
                uf.union(x, ~y)

        return len(stones) - len({uf.find(~y) for x, y in stones})
