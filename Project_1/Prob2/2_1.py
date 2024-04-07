
MAX_DEPTH = 900
input_matri = input()
matri = [str(item) for item in input_matri.split()]
move = [-1, 1, -3, 3]

correct_matri = ['1','2','3','4','5','6','7','8','x']

searched_condition = set()

def dfs(matri, correct_matri, depth=0):
    global searched_condition

    if matri == correct_matri:
        return 1
    
    if tuple(matri) in searched_condition:
        return 0
    else:
        searched_condition.add(tuple(matri))

    if depth >= MAX_DEPTH:
          return 0

    x_index = matri.index('x')
    new_matri = [item for item in matri]

    if x_index % 3 != 0:
        new_matri[x_index], new_matri[x_index - 1] = new_matri[x_index - 1], new_matri[x_index]
        if dfs(new_matri, correct_matri, depth + 1):
                return 1

    new_matri = [item for item in matri]    
    if  x_index % 3 != 2:
        new_matri[x_index], new_matri[x_index + 1] = new_matri[x_index + 1], new_matri[x_index]
        if dfs(new_matri, correct_matri, depth + 1):
                return 1

    new_matri = [item for item in matri]
    if x_index > 2:
        new_matri[x_index], new_matri[x_index - 3] = new_matri[x_index - 3], new_matri[x_index]
        if dfs(new_matri, correct_matri, depth + 1):
                return 1

    new_matri = [item for item in matri]
    if x_index < 6:
        new_matri[x_index], new_matri[x_index + 3] = new_matri[x_index + 3], new_matri[x_index]
        if dfs(new_matri, correct_matri, depth + 1):
                return 1

    return 0

print(dfs(matri, correct_matri))