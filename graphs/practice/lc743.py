from heapq import heappop, heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        
        for src, target, time in times:
            adj[src-1].append((target-1, time))
        
        dist = [10**18]*n
        dist[k-1] = 0
        
        heap = []
        heappush(heap, (0, k-1))  #(time, node)
        
        visited = [False]*n
        
        while(heap):
            _, node = heappop(heap)
            
            if(visited[node] == True):
                continue
            visited[node] = True
            
            for neighNode, weight in adj[node]:
                if(dist[neighNode] > dist[node] + weight):
                    dist[neighNode] = dist[node] + weight
                    heappush(heap, (dist[neighNode], neighNode))
        mx = max(dist)
        # print(dist)
        if(mx==10**18):
            return -1
        return mx
