'''
Problem Statement: https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1
'''

from heapq import heappush, heappop

def dijkstra(self, V, adj, S):
        dist = [0]*V
        for i in range(V):
            if(i!=S):
                dist[i] = 10**18
        heap = []
        heappush(heap, (0, S))
        
        while(heap):
            distance, node = heappop(heap)
            for neighNode, weight in adj[node]:
                if(dist[neighNode] > dist[node] + weight):
                    dist[neighNode] = dist[node] + weight
                    heappush(heap, (dist[neighNode], neighNode))
        return dist
