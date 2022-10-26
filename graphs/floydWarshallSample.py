'''All pair shortest path algorithm'''

dist = list2d(n+1,n+1,0)

graph = defaultdict(int)

for _ in range(m):
    a,b,c = MAP()
    if(graph[(a,b)] or graph[(b,a)]):
        graph[(a,b)] = min(graph[(a,b)], c)
        graph[(b,a)] = min(graph[(a,b)], c)
    else:
        graph[(a, b)] = c
        graph[(b,a)] = c

# initializing the dist matrix below:
for i in range(1, n+1):
    for j in range(1, n+1):
        if(i!=j):
            if(graph[(i,j)]):
                dist[i][j] = graph[(i,j)]
            else:
                dist[i][j] = INF

#FW algo below:
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
