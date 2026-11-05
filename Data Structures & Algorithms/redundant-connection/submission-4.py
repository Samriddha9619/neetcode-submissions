class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        par=[i for i in range(n+1)]
        rank=[1]*(n+1)
        def find(node):
            while node!=par[node]:
                par[node]=par[par[node]]
                node=par[node]
            return node
        for u,v in edges:
            p1,p2=find(u),find(v)

            if p1==p2:
                return [u,v]
            par[p1]=p2
        return []
