# 5 7
# 0 1 10
# 0 2 5
# 1 2 3
# 1 3 1
# 2 3 9
# 2 4 2
# 3 4 8

n,m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))  # If the graph is undirected

for i in range(n):  
    print(f"Node {i}: ", end="")
    for neighbor, weight in graph[i]:
        print(f"({neighbor},{weight}) ", end="")
    print()