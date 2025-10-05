

n,m = map(int,input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u) # for undirected graph

def bfs(s):
    from collections import deque
    q = deque()
    q.append(s)
    vis = [False] * n
    vis[s] = True
    while q:
        cur = q.popleft()
        print(cur,end=" ")
        for ngb in graph[cur]:
            if not vis[ngb]:
                vis[ngb] = True
                q.append(ngb)
bfs(0)

