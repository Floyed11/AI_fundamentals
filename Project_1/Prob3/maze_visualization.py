"""
待补充代码：对搜索过的格子染色
"""
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def visualize_maze_with_path(maze, path, color_map):
    plt.figure(figsize=(len(maze[0]), len(maze)))  # 设置图形大小
    plt.imshow(maze, cmap='Greys', interpolation='nearest')  # 使用灰度色图，并关闭插值

    # 绘制路径
    if path:
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, marker='o', markersize=8, color='red', linewidth=3)

    # 设置坐标轴刻度和边框
    plt.xticks(range(len(maze[0])))
    plt.yticks(range(len(maze)))
    plt.gca().set_xticks([x - 0.5 for x in range(1, len(maze[0]))], minor=True)
    plt.gca().set_yticks([y - 0.5 for y in range(1, len(maze))], minor=True)
    plt.grid(which="minor", color="black", linestyle='-', linewidth=2)

    # 显示障碍物
    cmap = ListedColormap(['lightblue', 'deepskyblue'])
    plt.imshow(maze, cmap=cmap, interpolation='nearest', alpha= 0.5)

    # 显示颜色
    cmap = ListedColormap(['lightblue', 'dodgerblue', 'royalblue', 'midnightblue'])
    plt.imshow(color_map, cmap=cmap, interpolation='nearest', alpha= 0.5)

    # 显示终点和起点
    plt.plot(0, 0, marker='o', markersize=20, color='yellow')
    plt.plot(len(maze[0]) - 1, len(maze) - 1, marker='*', markersize=20, color='yellow')

    plt.axis('on')  # 显示坐标轴
    plt.show()

# 提供迷宫的二维数组
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]

# 假设给定路径的坐标列表
path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]

# 记录走过的路径 0: 未走过  1: 走过  2: 走过且为选择的路径 3: 可以选择但没有走的路径
color_map = [
    [2, 1, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 2]
]

# 可视化迷宫及路径
# visualize_maze_with_path(maze, path, color_map)
