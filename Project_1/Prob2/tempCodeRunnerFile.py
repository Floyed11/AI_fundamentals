from queue import PriorityQueue

input_matri = input()
matri = [str(item) for item in input_matri.split()]

searched_matri = []

correct_matri = ['1','2','3','4','5','6','7','8','x']

move = [-1, 1, -3, 3]
move_name = ['l', 'r', 'u', 'd']

class Node:
    def __init__(self, matri, depth, value, route = ''):
        self.matri = matri
        self.value = value
        self.depth = depth
        self.route = route

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


def heuristic_func(current_matri, correct_matri):

    value = 0
    for i in range(9):
        if current_matri[i] == 'x':
            continue
        if current_matri[i] != correct_matri[i]:
            correct_index = correct_matri.index(current_matri[i])
            value += abs(i // 3 - correct_index // 3) + abs(i % 3 - correct_index % 3)
    
    return value

def A_star(matri, correct_matri):
    global searched_matri
    search_queue = PriorityQueue()
    search_queue.put(Node(matri, 0, heuristic_func(matri, correct_matri)))
    while not search_queue.empty():
        current_node = search_queue.get()
        current_matri = current_node.matri
        current_depth = current_node.depth
        current_route = current_node.route

        if current_matri == correct_matri:
            return current_route
        if current_matri in searched_matri:
            continue
        else:
            searched_matri.append(current_matri)
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
            if tuple(new_matri) in searched_matri:
                continue
            value = current_depth + 1 + heuristic_func(new_matri, correct_matri)
            search_queue.put(Node(new_matri, current_depth + 1, value, current_route + move_name[i]))

    return -1

def inversion_pair(matri):
    count = 0
    for i in range(8):
        for j in range(i + 1, 9):
            if matri[i] != 'x' and matri[j] != 'x' and int(matri[i]) > int(matri[j]):
                count += 1
    return count

if inversion_pair(matri) % 2 != inversion_pair(correct_matri) % 2:
    print('unsolvable')
else:
    print(A_star(matri, correct_matri))