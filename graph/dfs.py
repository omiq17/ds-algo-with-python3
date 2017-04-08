def doDfs(graph, source, color):
    color[source] = 1

    for i in graph[source]:
        # print("i", i)
        if color[i] == 0:
            doDfs(graph, i, color)

    # when every adjacent has done, it will
    print("node", source)
    color[source] = 2

### Graph Representation (Adjacency List)
node, edge = map(int, input().split())
graph = [[] for x in range(node+1)]

for i in range(edge):
    node_1, node_2 = map(int, input().split())
    # inserting twice
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)

print("Graph Representation: ",graph)

color = [0] * (node+1)
print("Traversals: ")
doDfs(graph, 1, color)
