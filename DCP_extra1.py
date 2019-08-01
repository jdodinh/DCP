class GraphNode():
    def __init__(self, node):
        self.N = []             # List of nodes north of
        self.E = []
        self.S = []
        self.W = []
        self.name = node


instructions = ["A N B", "B NE C", "C E A"]
nodes = {}


def toggle_loc(loc):
    if loc == 'N':
        return 'S'
    if loc == 'E':
        return 'W'
    if loc == 'S':
        return 'N'
    if loc == 'W':
        return 'E'


def check_direction(node, dir, start_node):
    nd_list = getattr(node, dir)                    # get the list of nodes that are in that particular direction
    if start_node in nd_list:
        print('FALSE')
        quit()
        return False
    else:
        for nd in nd_list:
            check_direction(nodes[nd], dir, start_node) 
        return True

# def check_direction_2(node, dir, start_node):
#     nd_list = getattr(node, dir)                    #get the list of nodes that are in that particular direction
#     if start_node in nd_list:
#         print('FALSE')
#         quit()
#         return False
#     else:
#         for nd in nd_list:
#             check_direction_2(nodes[nd], dir, start_node) 
#         return True


def main():
    for line in instructions:
        # line = "A N B"
        line = line.split(' ')
        node_1 = line[0]
        node_2 = line[2]
        location = line[1]
        if node_1 not in nodes:
            nodes[node_1] = GraphNode(node_1)
        if node_2 not in nodes:
            nodes[node_2] = GraphNode(node_2)
        for loc in location:
            getattr(nodes[node_2], loc).append(node_1)
            loc_inv = toggle_loc(loc)
            getattr(nodes[node_1], loc_inv).append(node_2)

    for node in nodes:
        start = nodes[node].name
        check_direction(nodes[node], 'N', start)
        check_direction(nodes[node], 'E', start)
        check_direction(nodes[node], 'S', start)
        check_direction(nodes[node], 'W', start)
        # name = node
        # node = nodes[node]
        # N_list = node.N
        # E_list = node.E
        # S_list = node.S
        # W_list = node.W
        # while E_list:
        #     if name in E_list:
        #         return False
        #     for nd in E_list:
        #         name = node
        #         node = nodes[node]





    for nd in nodes:
        name = nodes[nd].name
        N = nodes[nd].N
        E = nodes[nd].E
        S = nodes[nd].S
        W = nodes[nd].W
        print(name)
        print('N: ' + str(N))
        print('E: ' + str(E))
        print('S: ' + str(S))
        print('W: ' + str(W))

    

    




if __name__=="__main__":
    main()
    print('TRUE')