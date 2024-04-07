import maze_visualization as maze_visualization

n, m = map(int, input().split())

maze = [[0] * m for _ in range(n)]
color = [[0] * m for _ in range(n)]
color_map = [[0] * m for _ in range(n)]

for i in range(n):
    maze[i] = list(map(int, input().split()))

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
end = (n - 1, m - 1)
min_step = -1

path = []

def dfs(position, step, current_path):
    global min_step
    global path
    global color_map
    if position == end:
        if min_step == -1 or step < min_step:
            min_step = step
            path.append(end)
            path = current_path.copy()
        return
    
    if step >= min_step and min_step != -1:
        return
    x, y = position
    if (x < 0 or x >= n or y < 0 or y >= m) or maze[x][y] == 1 or color[x][y] == 1:
        return
    
    color[x][y] = 1
    color_map[x][y] = 1
    current_path.append((x, y))
    for i in range(4):
        new_x, new_y = x + move[i][0], y + move[i][1]
        dfs((new_x, new_y), step + 1, current_path)
    color[x][y] = 0
    current_path.pop()
    return

dfs((0, 0), 0, [])

for x, y in path:
    color_map[x][y] = 2

print(min_step)

print(color_map)
maze_visualization.visualize_maze_with_path(maze, path, color_map)
# print(path)