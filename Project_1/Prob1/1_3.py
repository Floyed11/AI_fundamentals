import heapq

n, m = map(int, input().split())

INF = 10 ** 10

dis = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)] #稀疏图，用链表存储

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    
start = 1
destination = n

def dijkstra_heap(graph, dis):
    Q = {i for i in range(1, n + 1)} #set加快查询速度
    dis[start] = 0
    graph_heap = [(dis[i], i) for i in range(1, n + 1)]
    heapq.heapify(graph_heap)
    while Q:
        d, u = heapq.heappop(graph_heap)
        if d == INF:
            break #说明已经没有可以松弛的边
        if u in Q:
            Q.remove(u) #防止重复访问
        else:
            continue
        for v, len in graph[u]:
            if (dis[v] > dis[u] + len):
                dis[v] = dis[u] + len
                heapq.heappush(graph_heap, (dis[v], v))

    if (dis[destination] == INF):
        return -1
    else:
        return dis[destination]

print(dijkstra_heap(graph, dis))