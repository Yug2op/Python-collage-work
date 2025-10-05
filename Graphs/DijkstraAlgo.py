# 5 7
# 0 1 10
# 0 2 5
# 1 2 3
# 1 3 1
# 2 3 9
# 2 4 2
# 3 4 8
import heapq
n,m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))  # If the graph is undirected
    
s = 0
min_heap = []

dis = [float('inf')] * n
dis[s] = 0
expl = [False] * n

for  i,d in enumerate(dis):
    heapq.heappush(min_heap, (d,i))

while min_heap:
    d,u = heapq.heappop(min_heap)
    if expl[u]:
        continue
    expl[u] = True
    for v,w in graph[u]:
        if not expl[v] and dis[u] + w < dis[v]:
            dis[v] = dis[u] + w
            heapq.heappush(min_heap, (dis[v], v))
for i in range(n):
    print(f"Distance from node {s} to node {i} is {dis[i]}")
# time: O((V + E) log V)
# space: O(V)

# correctness of dijkstra's algorithm:
# 1. Initialization: The algorithm starts by initializing the distance to the source node as 0 and all other nodes as infinity. This is correct because the shortest path from the source to itself is 0, and initially, we assume that all other nodes are unreachable.
# 2. Priority Queue: The algorithm uses a priority queue (min-heap) to always expand the least costly node first. This ensures that when a node is processed, the shortest path to that node has already been found.
# 3. Relaxation: For each node, the algorithm checks its neighbors and updates their distances if a shorter path is found through the current node. This step is crucial and is based on the principle that if the shortest path to a node is known, then the shortest path to its neighbors can be updated accordingly.
# so we use a algo to over come these problem that is bellman ford algorithm