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
    
for i in range(n):
    if not vis[i]:
        print(f"Component({i}):" ,end=" ")
        dfs(i)
        print()