class Solution:
    def find(self, x):
        while(x!=rep[x]):
            x = rep[x]
        return x
    
    def same(self, a, b):
        return self.find(a) == self.find(b)
        
    def combine(self, a, b):
        a = self.find(a)
        b = self.find(b)
        
        if(a==b):
            return 
        else:
            if(size[a]>size[b]):
                rep[b] = a
                size[a]+=size[b]
            else:
                rep[a] = b
                size[b]+=size[a]
        return
            
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        global rep
        global size
        
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                edges.append([i, j, abs(x1-x2) + abs(y1-y2)])
        
        edges.sort(key = lambda x:x[2])
        
        rep = list(range(n))
        size = [1]*n
        
        ans = 0
        edges_used = 0
        
        for edge in edges:
            node1, node2, distance = edge
            if(not self.same(node1, node2)):
                ans+=distance
                edges_used+=1
                self.combine(node1, node2)
                if(edges_used==n-1):
                    break
        return ans
