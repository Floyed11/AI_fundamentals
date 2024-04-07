n, m = map(int, input().split())

INF = -1

class Graph:
    def __init__(self, n, m, start=1, destination=None):
        self.m = m
        self.n = n
        self.graph = [[] for _ in range(n + 1)]
        self.color = [0] * (n + 1)
        self.start = start
        self.destination = destination if destination else n
        self.d = [INF] * (n + 1)

g = Graph(n, m)

for i in range(m):
    a, b = map(int, input().split())
    g.graph[a].append(b)

def bfs(g):
    g.d[g.start] = 0
    queue = []
    queue.append(g.start)
    while queue:
        u = queue.pop(0)
        if u == g.destination: # 必须先判断，防止有自环
            return g.d[u]
        for v in g.graph[u]:
            if g.color[v] == 0:
                g.color[v] = 1
                g.d[v] = g.d[u] + 1
                queue.append(v)
            else:
                continue
        g.color[u] = 2
    return -1

print(bfs(g))