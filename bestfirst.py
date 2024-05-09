def inputstates():
    puzzle = []
    for i in range(3):
        a = [x for x in input().split(' ')]
        puzzle.append(a)
    return puzzle

def drawstate(puzzle):
    for i in range(3):
        for j in range(3):
            print(puzzle[i][j], end=" ")
        print(" ")
    print("")

def indexpos(goal, value):
    for i in range(3):
        for j in range(3):
            if goal[i][j] == value:
                return (i, j)

def heuristic(start, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if start[i][j] != '0':
                x, y = indexpos(goal, start[i][j])
                count = count + abs(x - i) + abs(y - j)
    return count

def movegen(puzzle):
    X, Y = 0, 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == "0":
                X, Y = i, j
                break
    templist = [(X + 1, Y), (X - 1, Y), (X, Y + 1), (X, Y - 1)]
    templist = [x for x in templist if x[0] >= 0 and x[0] <= 2 and x[1] >= 0 and x[1] <= 2]
    newstate = []
    for x in templist:
        new = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                new[i][j] = puzzle[i][j]
        new[X][Y] = puzzle[x[0]][x[1]]
        new[x[0]][x[1]] = '0'
        newstate.append(new)
    return newstate

def eight_puzzle():
    print("Enter the initial state: ")
    start = inputstates()
    print("Enter the goal state: ")
    goal = inputstates()

    queue = [(start, "nil", heuristic(start, goal))]
    open = [(start, "nil")]
    closed = []
    flag = 0

    while len(queue) > 0:
        a = queue.pop(0)
        closed.insert(0, (a[0], a[1]))
        open.remove((a[0], a[1]))
        if a[2] == 0:
            flag = 1
            break
        temp = movegen(a[0])
        temp = [(x, a[0]) for x in temp]
        temp = [x for x in temp if x not in open and x not in closed]
        open.extend(temp)
        temp = [(x[0], x[1], heuristic(x[0], goal)) for x in temp]
        queue = temp + queue
        queue = sorted(queue, key=lambda x: x[2])

    if flag == 1:
        print("\n\nThe solution for 8puzzle : \n")
        path = []
        cur = goal
        for i in closed:
            if i[0] == cur:
                path.insert(0, i[0])
                cur = i[1]
        step = 1
        for i in path:
            print("Step: ", step, "\n")
            drawstate(i)
            step += 1
        print("Total number of steps: ", len(path))
    else:
        print("No solution found")

eight_puzzle()
 
 
