class Solution:
            
    def equationsPossible(self, equations: List[str]) -> bool:
        class UnionFind:
            def __init__(self,n):
                self.parents = list(range(n))

            def find(self, x):
                if self.parents[x] != x:
                    self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

            def union(self,x,y):
                root_x = self.find(x)
                root_y = self.find(y)
                if root_x != root_y:
                    self.parents[root_x] = root_y
        uf = UnionFind(26)
        for eq in equations:
            if eq[1] == "=" :
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                uf.union(x,y)
        for eq in equations:

            if eq[1] == "!":
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                root_x= uf.find(x)
                root_y = uf.find(y)
                if root_x == root_y:
                    return False
        return True
        