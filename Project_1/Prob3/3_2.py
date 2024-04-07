import maze_visualization as maze_visualization

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

def bfs(start):
    global min_step
    global color_map
    queue = []
    queue.append(start)
    while queue:
        position = queue.pop(0)
        if position == end:
            return
        x, y = position
        color[x][y] = 1
        color_map[x][y] = 1
        print(position)

        for i in range(4):
            new_x, new_y = x + move[i][0], y + move[i][1]
            if (new_x <0 or new_x >= n or new_y < 0 or new_y >= m) or maze[new_x][new_y] == 1 or color[new_x][new_y] == 1:
                continue
            queue.append((new_x, new_y))
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

bfs((0, 0))
get_path((0, 0))
min_step = len(path) - 1
print(min_step)
for x, y in path:
    color_map[x][y] = 2
# print(path)

maze_visualization.visualize_maze_with_path(maze, path, color_map)