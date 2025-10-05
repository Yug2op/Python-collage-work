# 9 12
# 0 1
# 0 2
# 1 3
# 1 4
# 2 4
# 2 5
# 3 6
# 4 6
# 4 7
# 5 7
# 6 8
# 7 8
from collections import deque

n,m = map(int,input().split())

adj = [[] for _ in range(n)]

for _ in range(m):
    u,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
    
s = 0
vis = [False] * n
q = deque()

vis[s] = True
q.append(s)

dis = [None] * n
dis[s] = 0

while q:
    cur = q.popleft()
    for ngb in adj[cur]:
        if not vis[ngb]:
            vis[ngb] = True
            q.append(ngb)
            dis[ngb] = dis[cur] + 1
            
for i in range(n):
    print(f"dis({i}) = {dis[i]}")