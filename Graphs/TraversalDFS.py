# the key idea behind the DFS algorithm is that for any vertwx "u",
# in the graph, when you visit one of its unvisited neighbour, say"v",
# then you first you visit all the unvisited neighbours of "v"
# before you visit any other unvisited neighbour of "u"
# this is done using recursion or using a stack data structure

n,m = map(int,input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u) # for undirected graph

s = 0

vis = [False] *n

def dfs(cur):
    vis[cur] = True
    print(cur,end=" ")
    for ngb in graph[cur]:
        if not vis[ngb]:
            dfs(ngb)   
    
    
dfs(s)
    
    
    
    
    
    
    
    
