f = 0
t = 1

maze = [
    [f, f, f, f],
    [t, t, f, t],
    [f, f, f, f],
    [f, f, f, f]
]
start_coord = (2, 0)
end_coord = (0, 0)



class graph_element:
    def __init__(self, coord, color, typ, level):
        self.coord = coord
        self.color = color
        self.typ = typ
        self.level = level
        self.parent = None

    


def BFS_graph(start_node, end_node, grph):
    width = len(grph[0])
    height = len(grph)
    queue = []
    elem = start_node
    elem.level = 0
    queue.append(elem)
    lev = 0
    while queue:
        v = queue.pop(0)
        v.color = 'gray'
        row = v.coord[0]
        col = v.coord[1]
        lev = v.level
        if row > 0:
            node = grph[row-1][col]
            if (node.typ == 0) and (node.color == 'white'):
                node.color = 'gray'
                node.level = lev + 1
                node.parent = v
                queue.append(node)
        if col > 0:
            node = grph[row][col-1]
            if (node.typ == 0) and (node.color == 'white'):
                node.color = 'gray'
                node.level = lev + 1
                node.parent = v
                queue.append(node)

        # if i reverse the following two if statements the code works, else it outputs the wrong value. 
        if (width - col - 1 > 0):
            node = grph[row][col+1]
            if (node.typ == 0) and (node.color == 'white'):
                node.color = 'gray'
                node.level = lev + 1
                node.parent = v
                queue.append(node)
        if (height - row - 1 > 0):
            node = grph[row+1][col]
            if (node.typ == 0) and (node.color == 'white'):
                node.color = 'gray'
                node.level = lev + 1
                node.parent = v
                queue.append(node)

        
        
        v.color = 'black'
        # print_graph(grph)
    return end_node.level



def print_graph(grph):
    for line in grph:
        for node in line:
            if (node.typ == 1):
                print('XX', end=" ")
            else:
                print(node.color[0], node.level, sep="", end=" ")
        print()
    print()



def main ():
    graph = []
    s_row = start_coord[0]
    s_col = start_coord[1]
    t_row = end_coord[0]
    t_col = end_coord[1]
    for i in range(len(maze)):
        graph_row = []
        row = maze[i]
        for j in range(len(row)):
            elem = graph_element((i, j), 'white', maze[i][j], -1)
            graph_row.append(elem)
        graph.append(graph_row)
    start = graph[s_row][s_col]
    stop = graph[t_row][t_col]
    steps = BFS_graph(start, stop, graph)
    print(steps)
        

if __name__ == "__main__":
    main()