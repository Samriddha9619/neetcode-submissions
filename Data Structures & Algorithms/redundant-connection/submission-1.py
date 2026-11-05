class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        par=[i for i in range(n+1)]
        rank=[1]*(n+1)
        def find(node):
            if node==par[node]:
                return node
            else:
                return find(par[node])

        def union(u,v):
            p1,p2=find(u),find(v)
            if p1==p2:
                return False
            if rank[p1]>rank[p2]:
                par[p2]=p1
                rank[p1]+=1
            else:
                par[p1]=p2
                rank[p2]+=1
            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v]
        return []
