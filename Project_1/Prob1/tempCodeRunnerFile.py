import heapq

n, m = map(int, input().split())

INF = 10 ** 10

dis = [INF] * (n + 1)
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(m):
    x, y, z = map(int, input().split())
    if (graph[x][y] == INF or graph[x][y] > z): #考虑重边的情况
        graph[x][y] = z
start = 1
destination = n

def dijkstra_heap(graph, dis):
    Q = [i for i in range(1, n + 1)]
    dis[start] = 0
    graph_heap = [(dis[i], i) for i in range(1, n + 1)]
    heapq.heapify(graph_heap)
    while Q:
        d, u = heapq.heappop(graph_heap)
        if d == INF:
            return -1
        Q.remove(u)
        for v in range(1, n + 1):
            if graph[u][v] < INF:
                if (dis[v] > dis[u] + graph[u][v]) or (dis[v] == INF):
                    dis[v] = dis[u] + graph[u][v]
                    heapq.heappush(graph_heap, (dis[v], v))

    return dis[destination]

print(dijkstra_heap(graph, dis))