"""
Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or
alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and
the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an
infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live
cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""

import copy


def count(x_val, y_val, map):
    living_n = 0
    dead_n = 0
    for i in range(x_val-1, x_val+2):
        if map[y_val-1][i] == "*":
            living_n += 1
        else:
            dead_n += 1
        if map[y_val+1][i] == "*":
            living_n += 1
        else:
            dead_n += 1
    if map[y_val][x_val-1] == "*":
        living_n += 1
    else:
        dead_n += 1
    if map[y_val][x_val+1] == "*":
        living_n += 1
    else:
        dead_n += 1

    return living_n, dead_n


def step(map, x_off, y_off):
    living_cells = []
    for y in range(1, len(map)-1):
        for x in range(1, len(map[y])-1):
            liv, ded = count(x, y, map)
            if map[y][x] == "*" and liv < 2:
                pass
            elif map[y][x] == "*" and (liv == 2 or liv == 3):
                living_cells.append((x+x_off, y+y_off))
            elif map[y][x] == "*" and liv > 3:
                pass
            elif map[y][x] == "." and liv == 3:
                living_cells.append((x + x_off, y + y_off))
            elif map[y][x] == "*":
                living_cells.append((x + x_off, y + y_off))
    return living_cells


def maxes(cells):
    living_cells = cells
    x_min = living_cells[0][0]
    x_max = living_cells[0][0]
    y_min = living_cells[0][1]
    y_max = living_cells[0][1]
    for el in living_cells:
        if x_min > el[0]:
            x_min = el[0]
        if x_max < el[0]:
            x_max = el[0]
        if y_min > el[1]:
            y_min = el[1]
        if y_max < el[1]:
            y_max = el[1]
    matrix = []
    for i in range(y_min - 1, y_max + 2):
        row = []
        for j in range(x_min - 1, x_max + 2):
            row.append('.')
        matrix.append(row)
    # for cell in living_cells:
    #     matrix[cell[1] - y_min+1][cell[0] - x_min+1] = "*"
    return matrix, x_min, y_min


def print_matrix(mtx):
    mtx = copy.deepcopy(mtx)
    mtx.reverse()
    for row in mtx:
        for el in row:
            print(el, end=" ")
        print("\n", end="")


def main():
    steps = 5
    living_cells = [(-1, 3), (2, 6), (1, 5), (2, 2), (3, 1), (3, 2), (3, 3), (3, 5), (-9, 10)]
    matrix, x_off, y_off = maxes(living_cells)
    temp_mat = copy.deepcopy(matrix)
    for cell in living_cells:
        temp_mat[cell[1] - y_off+1][cell[0] - x_off+1] = "*"
    # matrix.reverse()
    # matrix = step(matrix)
    print_matrix(temp_mat)
    for i in range(steps):
        print("\n-------------\n")
        living_cells = step(temp_mat, x_off, y_off)
        if len(living_cells) == 0:
            print("no living cells left")
            break
        #matrix, x_off, y_off = maxes(living_cells)
        temp_mat = copy.deepcopy(matrix)
        for cell in living_cells:
            temp_mat[cell[1] - y_off][cell[0] - x_off] = "*"
        print_matrix(temp_mat)


if __name__ == '__main__':
    main()