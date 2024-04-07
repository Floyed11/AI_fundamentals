from queue import PriorityQueue

input_matri = input()
matri = [str(item) for item in input_matri.split()]

correct_matri = ['1','2','3','4','5','6','7','8','x']

move = [-1, 1, -3, 3]
searched_matri = set()

class Node:
    def __init__(self, matri, value):
        self.matri = matri
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

search_loop = 0

def dijkstra(matri):
    queue = PriorityQueue()
    queue.put(Node(matri, 0))
    while not queue.empty():
        current_node = queue.get()
        current_matri = current_node.matri
        current_value = current_node.value

        if current_matri == correct_matri:
            return current_value
        if tuple(current_matri) in searched_matri:
            continue
        else:
            searched_matri.add(tuple(current_matri))

        x_index = current_matri.index('x')

        for i in range(4):
            move_step = move[i]
            move_index = x_index + move_step
            if move_index < 0 or move_index >= 9:
                continue
            if (x_index % 3 == 0 and move_step == -1) or (x_index % 3 == 2 and move_step == 1):
                continue
            new_matri = [item for item in current_matri]
            new_matri[x_index], new_matri[move_index] = new_matri[move_index], new_matri[x_index]
            if tuple(new_matri) in searched_matri: #防止加入多余的节点
                continue
            queue.put(Node(new_matri, current_value + 1))
    
    return -1


def inversion_pair(matri):
    count = 0
    for i in range(8):
        for j in range(i + 1, 9):
            if matri[i] != 'x' and matri[j] != 'x' and int(matri[i]) > int(matri[j]):
                count += 1
    return count

if inversion_pair(matri) % 2 != inversion_pair(correct_matri) % 2:
    print(-1)
else:
    print(dijkstra(matri))
