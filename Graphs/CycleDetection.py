n,m = map(int,input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u) # for undirected graph

s = 0

vis = [False] *n

def dfs(u,p):
    vis[u] = True
    for v in graph[u]:
        if not vis[v]:
            if dfs(v,u):
                return True
        else:
            if p != v:
                return True
    return False

flag = False
for i in range(n):
    if not vis[i]:
        if dfs(i,-1):
            flag = True
            print("Cycle Detected")
            break

if not flag:
    print("No cycle")
