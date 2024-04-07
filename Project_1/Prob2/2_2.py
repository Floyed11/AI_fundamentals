from collections import deque
input_matri = input()
matri = [str(item) for item in input_matri.split()]

correct_matri = ['1','2','3','4','5','6','7','8','x']

search_queue = deque() #出队的时间复杂度为O（1），远优于list的O（n）
searched = set()
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]


search_loop = 0

# def toString(matri):
#     result = ''
#     for i in matri:
#         result += i
#     return result

def bfs(search_matri):
    global search_queue
    global searched
    global search_loop

    search_queue.append([search_matri, 0])

    while (search_queue):
        matri, depth = search_queue.popleft()
        
        if (tuple(matri) in searched): #同个状态有可能被多次加入队列
            continue
        else:
            searched.add(tuple(matri))

        if matri == correct_matri:
            return depth
        new_matri = [item for item in matri]
        index = matri.index('x')
        x_index = index % 3
        y_index = index // 3
        
        for i in range(4):
            new_matri = [item for item in matri]

            new_x_index = x_index + move[i][0]
            new_y_index = y_index + move[i][1]
            if new_x_index < 0 or new_x_index > 2 or new_y_index <0 or new_y_index > 2:
                continue
            new_matri[index], new_matri[new_x_index + new_y_index * 3] = new_matri[new_x_index + new_y_index * 3], new_matri[index]
            if tuple(new_matri) in searched:
                continue
            else:
                search_queue.append([new_matri, depth + 1])



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
    print(bfs(matri))