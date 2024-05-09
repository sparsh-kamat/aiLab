def Astar(graph, heuristic):
    Snode = input("Enter the starting node: ")
    Enode = input("Enter the ending node: ")
    # open(node, parent, distance from goal, heuristic, total cost)
    open_list = [(Snode, None, 0, heuristic[Snode], 0 + heuristic[Snode])]
    closed = []
    parent = {Snode: None}
    traversal = []
    while len(open_list) > 0:
        state = open_list.pop(0)
        traversal.append(state)
        temp = [(x, state[0], state[2] + graph[state[0]][x], heuristic[x], state[2] + graph[state[0]][x] + heuristic[x]) for x in graph[state[0]].keys() if x not in closed]
        # Assign parent for new nodes
        for x in temp:
            parent[x[0]] = state[0]
        if state[0] == Enode: # end node is found
            break
        # Insert into open list and sort it based on cost+heuristic
        open_list = temp + open_list
        open_list = sorted(open_list, key=lambda x: x[4])
        # Insert into closed list
        closed.append(state[0])
    # Reconstruct path
    current = Enode
    path = [Enode]
    while current != Snode:
        path.insert(0, parent[current])
        current = parent[current]
    print("Traversal: ", end="")
    prev = None
    for node in traversal:
        if node[0] in path and node[1] is prev:
            print(node, end=" ")
        prev = node[0]
    # Print path
    print("\n\nPath: ", end="")
    for i in path:
        print(i, end="\n" if i == Enode else "->")

graph = {
    'A': {'B': 11, 'D': 32, 'H': 36},
    'B': {'A': 11, 'C': 24, 'K': 42},
    'C': {'B': 24, 'E': 40},
    'D': {'S': 25, 'A': 32, 'F': 24, 'I': 26},
    'E': {'C': 40, 'K': 32},
    'F': {'D': 24, 'L': 27},
    'H': {'J': 22, 'A': 36, 'K': 28, 'N': 44},
    'G': {'T': 32, 'N': 42},
    'I': {'D': 26, 'L': 21, 'M': 32},
    'J': {'M': 20, 'H': 22},
    'K': {'B': 42, 'E': 32, 'H': 28, 'N': 27, 'Q': 62},
    'L': {'F': 27, 'O': 26, 'I': 21},
    'M': {'I': 32, 'P': 23, 'J': 20},
    'N': {'H': 44, 'K': 27, 'Q': 32, 'G': 42},
    'O': {'L': 26, 'R': 27},
    'P': {'M': 23},
    'Q': {'K': 62, 'N': 32},
    'R': {'O': 27, 'T': 52},
    'S': {'D': 25},
    'T': {'R': 52, 'G': 32}
}

# distance from goal
heuristic = {
    'A': 11, 'B': 10, 'C': 8, 'D': 12, 'E': 5,
    'F': 12, 'G': 0, 'H': 8, 'I': 10, 'J': 8,
    'K': 6, 'L': 10, 'M': 7, 'N': 4, 'O': 8,
    'P': 5, 'Q': 1, 'R': 6, 'S': 14, 'T': 2
}

# Call the A* algorithm function
Astar(graph, heuristic) 
