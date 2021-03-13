'''
Input:
8 13
1 4 15
1 5 8
1 6 2
4 3 12
4 5 6
3 5 30
3 2 7
3 8 3
8 2 2
2 7 2
7 6 1
2 5 9
5 6 5
'''
def dijkstra(n, graph, v):
    d = [99999] * n
    used = [False] * n
    way = [None] * n
    u = None
    d[v - 1] = 0
    way[v - 1] = -1
    for step in range(n):
        #Шаг 1. Найти среди непросмотренных вершин минимальную. Это будет вершина u
        minR = 100000
        for i in range(n):
            isUsed = used[i]
            if not isUsed and d[i] < minR:
                u = i + 1
                minR = d[i]
        #Шаг 2. Отметить вершину u как просмотренную
        used[u - 1] = True
        #Шаг 3. Для всех вершин w существует ребро (u; w) и сделать проверку на релаксацию
        for pair in matrix[u]:
            w = pair[0]
            weight = pair[1]
            if d[w - 1] > d[u - 1] + weight:
                d[w - 1] = d[u - 1] + weight
                way[w - 1] = u
    return [d, way]
n, m = map(int, input().split())
matrix = {}
for _ in range(m):
    a, b, c = map(int, input().split())
    if a not in matrix:
        matrix[a] = []
    if b not in matrix:
        matrix[b] = []
    matrix[a].append([b, c])
    matrix[b].append([a, c])

distance, way = dijkstra(n, matrix, 1)