import maze_visualization as maze_visualization

from queue import PriorityQueue
n, m = map(int, input().split())

maze = [[0] * m for _ in range(n)]
color = [[0] * m for _ in range(n)]
prev = [[0, 0] * m for _ in range(n)]
color_map = [[0] * m for _ in range(n)]

for i in range(n):
    maze[i] = list(map(int, input().split()))

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
end = (n - 1, m - 1)
min_step = -1
path = []

class Node:
    def __init__(self, position, lenth):
        self.position = position
        self.lenth = lenth

    def __lt__(self, other):
        self.lenth < other.lenth

    def __gt__(self, other):
        self.lenth > other.lenth

def dijkstra(start):
    global min_step
    global color_map
    queue = PriorityQueue()
    queue.put(Node(start, 0))
    while not queue.empty():
        node = queue.get()
        x, y = node.position
        if node.position == end:
            min_step = node.lenth
            return
        color[x][y] = 1
        color_map[x][y] = 1
        for i in range(4):
            new_x, new_y = x + move[i][0], y + move[i][1]
            if (new_x <0 or new_x >= n or new_y < 0 or new_y >= m) or maze[new_x][new_y] == 1 or color[new_x][new_y] == 1:
                continue
            queue.put(Node((new_x, new_y), node.lenth + 1))
            prev[new_x][new_y] = [x, y]
    return

def get_path(start):
    global path
    x, y = end
    while (x, y) != start:
        path.append((x, y))
        x, y = prev[x][y]
    path.append(start)
    path.reverse()
    return

dijkstra((0, 0))
get_path((0, 0))
for x, y in path:
    color_map[x][y] = 2
print(min_step)
maze_visualization.visualize_maze_with_path(maze, path, color_map)