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

def dijkstra(graph, dis):
    S = []
    Q = [i for i in range(1, n + 1)]
    dis[start] = 0
    while Q:
        u = Q[0]
        for i in Q:
            if dis[i] < dis[u]:
                u = i

        if dis[u] == INF:
            break
        
        Q.remove(u)
        for v in range(1, n + 1):
            if graph[u][v] < INF:
                if (dis[v] > dis[u] + graph[u][v]) or (dis[v] == INF):
                    dis[v] = dis[u] + graph[u][v]
    if (dis[destination] == INF):
        return -1
    else:
        return dis[destination]

print(dijkstra(graph, dis))