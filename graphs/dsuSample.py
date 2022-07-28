'''
Define global variables rep (initialize with all index values) and size (initialize with all 1s) of length n (number of nodes)

rep = list(range(n))
size = [1]*n

'''
def find(x):
    while(x!=rep[x]):
        x = rep[x]
    return x

def same(a, b):
    return find(a) == find(b)

def combine(a, b):
    a = find(a)
    b = find(b)

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
  
'''
MST driver code:

#edges should be sorted
for edge in edges:
    node1, node2, distance = edge
    if(not self.same(node1, node2)):
        ans+=distance
        edges_used+=1
        self.combine(node1, node2)
        if(edges_used==n-1):
            break
'''
