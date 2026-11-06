class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h=[]
        for x,y in points :
            dis=(x*x)+(y*y)
            h.append([dis,x,y])
        heapq.heapify(h)
        res=[]
        while k>0:
            dis,x,y=heapq.heappop(h)
            res.append([x,y])
            k-=1

        return res