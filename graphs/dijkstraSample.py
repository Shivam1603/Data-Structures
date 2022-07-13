'''
Problem Statement: https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1
'''

def dijkstra(self, V, adj, S):
        dist = [0]*V
        for i in range(V):
            if(i!=S):
                dist[i] = 10**18
        heap = []
        heappush(heap, (0, S))
        
        visited = [False]*V
        
        while(heap):
            distance, node = heappop(heap)
            if(visited[node] == True):
                continue
            visited[node] = True
            for neighNode, weight in adj[node]:
                if(dist[neighNode] > dist[node] + weight):
                    dist[neighNode] = dist[node] + weight
                    heappush(heap, (dist[neighNode], neighNode))
        return dist
