class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        class UnionFind:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.rank = [1] * n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])  # Path compression
                return self.parent[x]

            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootX == rootY:
                    return False

                # Union by rank
                if self.rank[rootX] > self.rank[rootY]:
                    self.parent[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.parent[rootX] = rootY
                else:
                    self.parent[rootY] = rootX
                    self.rank[rootX] += 1
                return True

      
        uf = UnionFind(len(accounts))
        emailToAcc = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcc:
                    uf.union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i

       
        emailGroup = defaultdict(list)
       
        for email, i in emailToAcc.items():
            leader = uf.find(i)
          
            emailGroup[leader].append(email)
            
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]  
            res.append([name] + sorted(emails))

        return res
