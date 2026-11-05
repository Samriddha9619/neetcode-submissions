class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu=DSU(n)
        res=n
        for u,v in edges:
            if dsu.union(u,v):
                res-=1
        return res
        
class DSU:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[1]*n

    def find(self,node):
        cur=node
        while cur!=self.parent[cur]:
            self.parent[cur]=self.parent[self.parent[cur]]
            cur=self.parent[cur]
        return cur

    def union(self,u,v):
        parent_u=self.find(u)
        parent_v=self.find(v)

        if parent_u==parent_v:
            return False
        
        if self.rank[parent_v]>self.rank[parent_u]:
            parent_v,parent_u=parent_u,parent_v

        self.parent[parent_v]=parent_u
        self.rank[parent_u]+=self.rank[parent_v]
        return True