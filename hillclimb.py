import copy

def new_states(puzzle):
    new_states = [] #list to store new states
    for i in range(0, 3):
        for j in range(0, 3):
            if puzzle[i][j] == 0:
                if i - 1 >= 0: #up movement
                    temp = puzzle[i-1][j] #store above tile in temp
                    puzzle[i][j] = puzzle[i-1][j] #move above tile to current position
                    puzzle[i-1][j] = 0  #move blank tile to above tile position
                    new_states.append(copy.deepcopy(puzzle))
                    puzzle[i-1][j] = temp
                    puzzle[i][j] = 0

                if i + 1 < 3: #down Movement
                    temp = puzzle[i+1][j]
                    puzzle[i][j] = puzzle[i+1][j]
                    puzzle[i+1][j] = 0
                    new_states.append(copy.deepcopy(puzzle))
                    puzzle[i+1][j] = temp
                    puzzle[i][j] = 0

                if j - 1 >= 0: #left movement
                    temp = puzzle[i][j-1]
                    puzzle[i][j] = puzzle[i][j-1]
                    puzzle[i][j-1] = 0
                    new_states.append(copy.deepcopy(puzzle))
                    puzzle[i][j-1] = temp
                    puzzle[i][j] = 0

                if j + 1 < 3: #right Movement
                    temp = puzzle[i][j+1]
                    puzzle[i][j] = puzzle[i][j+1]
                    puzzle[i][j+1] = 0
                    new_states.append(copy.deepcopy(puzzle))
                    puzzle[i][j+1] = temp
                    puzzle[i][j] = 0
                break
    return new_states

def find_correct_tile(puzzle, goal):
    cnt = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if puzzle[i][j] == goal[i][j]:
                cnt += 1
    return cnt

def hill_climbing(start, goal):
    count = find_correct_tile(start, goal) #number of correct tiles
    max_count = count
    next_states = new_states(start) #possible next states
    current_state = start
    prev_state = start
    a = u'\u2193'

    while True:
        for state in next_states:
            count = find_correct_tile(state, goal)
            if count > max_count: #if true new state closer to goal
                current_state = state
                max_count = count

        if current_state == prev_state:
            print("\nLocal Minima reached")
            break

        print("\n    |")
        print("   ", a)
        print()

        for row in current_state:
            print(row)

        if current_state == goal:
            print("Solution found")
            break

        next_states = new_states(current_state)
        prev_state = current_state

goal = [[0,0,0], [0,0,0], [0,0,0]]
start = [[0,0,0], [0,0,0], [0,0,0]]

print("Enter the Start state")
for i in range(0, 3):
    for j in range(0, 3):
        start[i][j] = int(input())

print("Enter the Goal state")
for i in range(0, 3):
    for j in range(0, 3):
        goal[i][j] = int(input())

print("The start state is")
for row in start:
    print(row)

hill_climbing(start, goal)
 
