def dfs(graph, v):
	used.append(v)
	for neighbour in graph[v]:
		if neighbour not in used:
			dfs(graph, neighbour)

n, m = map(int, input().split())
graph = {}
for _ in range(m):
	a, b = map(int, input().split())
	if a not in graph.keys():
		graph[a] = []
	if b not in graph.keys():
		graph[b] = []
	graph[a].append(b)
	graph[b].append(a)

used = []
for v in range(1, n + 1):
	if v not in used:
		dfs(graph, v)
