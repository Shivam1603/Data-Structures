from heapq import heapify, heappush, heappop
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = defaultdict(list)
        
        for i in range(len(edges)):
            a, b = edges[i]
            pr = succProb[i]
            adj[a].append((b, pr))
            adj[b].append((a, pr))
        # print(adj)
        probab = [0]*n
        probab[start] = 1
        
        queue = []
        heappush(queue, (-1, start)) # (probability, node)
        
        visited = [False]*n
        
        while(queue):
            probability, node = heappop(queue)
            
            if(visited[node] == True):
                continue
            visited[node] = True
            
            for neighNode, weight in adj[node]:
                if(probab[neighNode] < probab[node]*weight):
                    probab[neighNode] = probab[node]*weight
                    
                    heappush(queue, (-probab[neighNode], neighNode))
        return probab[end]
