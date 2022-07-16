from heapq import heappush, heappop
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        effort = [[10**18]*m for _ in range(n)]
        effort[0][0] = 0
        visited = [[False]*m for _ in range(n)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        heap = []
        
        heappush(heap, (0, 0, 0))   #(effort, row, column)
        
        while(heap):
            _, r, c = heappop(heap)
            
            if(visited[r][c] == True):
                continue
            visited[r][c] = True
            
            for dirX, dirY in dirs:
                R, C = r + dirX, c + dirY
                if(R>=0 and R<n and C>=0 and C<m and visited[R][C]==False):
                    if(effort[R][C] > max(effort[r][c], abs(heights[r][c] - heights[R][C]))):
                        effort[R][C] = max(effort[r][c], abs(heights[r][c] - heights[R][C]))
                        heappush(heap, (effort[R][C], R, C))
#         print(effort)
        return effort[n-1][m-1]
