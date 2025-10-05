# graph is a non linear data structure consisting of nodes and edges
# nodes are also called vertices
# edges are the connections between the nodes
# graphs can be directed or undirected
# graphs can be weighted or unweighted
# graphs can be cyclic or acyclic

# adjacency list representation of graph

n,m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u) # for undirected graph
# print(graph)
for i in range(n):
    print(f"Node {i}: ", end='')
    for j in graph[i]:
        print(j, end=' ')
    print()
# space: O(n + m)
# time: O(n + m)
