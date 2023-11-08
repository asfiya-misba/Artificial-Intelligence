# AI Assignment 1
# Asfiya Misba - 1002028239
import sys
import itertools
import heapq
from collections import deque

flag = False
file = open('dump_file.txt', 'w')


class Node:
    def __init__(self, state, parent=None, moves=None, pathCost=0):
        self.state = state
        self.parent = parent
        self.moves = moves
        self.pathCost = pathCost
        self.depth = 0
        self.g = 0
        if parent:
            self.depth = parent.depth + 1

    # Method to find the path to the root
    def path(self):
        pathToRoot = []
        currentNode = self
        while currentNode is not None:
            pathToRoot.append(currentNode)
            currentNode = currentNode.parent
        return list(reversed(pathToRoot))

    # Method to expand the node
    def expand(self, problem):
        childNodes = []
        for move in problem.moves(self.state):
            childNode = self.childNode(problem, move)
            childNodes.append(childNode)
        return childNodes

    # Method to find the children
    def childNode(self, problem, moves):
        nextState = problem.result(self.state, moves)
        nextPathcost = problem.pathCost(self.pathCost, self.state, moves, nextState)
        nextNode = Node(nextState, self, moves, nextPathcost)
        return nextNode

    # Method to list the moves that make up the solution
    def solution(self):
        moves = []
        for i, node in enumerate(self.path()[1:], 1):
            move_str = node.moves
            if move_str:
                empty_tile_index = node.state.index(0)
                tile_number = node.state[empty_tile_index - 1]
                moves.append(f"Move {tile_number} {move_str}")
        return moves

    # method to compare 2 nodes based on their pathCost attribute
    def __lt__(self, other):
        return self.pathCost < other.pathCost

    def g(state):
        distance = 0
        for i in range(3):
            for j in range(3):
                tile = state[i][j]
                if tile != 0:
                    # calculate the correct position of the tile
                    row = (tile - 1) // 3
                    col = (tile - 1) % 3
                    # add the Manhattan distance to the correct position
                    distance += abs(i - row) + abs(j - col)
        return distance


class EightPuzzle:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    # Method to find the empty tile
    def emptyTile(self, state):
        return state.index(0)

    # Method to find the path cost
    def pathCost(self, cost, state1, moves, state2):
        return cost + 1

    # Method to check if the current state is the goal state
    def goalState(self, state):
        return state == self.goal

    # Method to find the next move to be performed
    def moves(self, state):
        movesAllowed = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        emptyIndex = self.emptyTile(state)
        if emptyIndex % 3 == 0:
            movesAllowed.remove('LEFT')
        if emptyIndex < 3:
            movesAllowed.remove('UP')
        if emptyIndex % 3 == 2:
            movesAllowed.remove('RIGHT')
        if emptyIndex > 5:
            movesAllowed.remove('DOWN')

        # result = [f"Move {emptyIndex + 1} {move}" for move in movesAllowed]
        # return result
        # print(movesAllowed)
        return movesAllowed

    # Method to find the sequence of moves leading to the goal state
    def result(self, state, moves):
        empty = self.emptyTile(state)
        new_state = list(state)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = empty + delta[moves]
        # print(neighbor.__index__())
        new_state[empty], new_state[neighbor] = new_state[neighbor], new_state[empty]
        # print(new_state) # board config changes
        if flag:
            file.write('Current board configuration is: ')
            file.write(str(new_state))
        return tuple(new_state)


# Breadth First Search
def BFS(problem):
    global node
    fringe = deque([node])  # Using deque instead of list (FIFO)
    exploredNodes = set()  # Using set instead of list
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 1  # Initial node is generated
    max_fringe_size = 1
    depth = 0
    while fringe:
        node = fringe.popleft()  # Using popleft() to remove the leftmost node
        nodes_popped += 1
        if node.state not in exploredNodes:
            exploredNodes.add(node.state)  # explored node
            if flag:
                file.write('Explored Nodes: ')
                file.write(str(exploredNodes))
            nodes_expanded += 1
        for moves in problem.moves(node.state):
            if flag:
                file.write('Move: ')
                file.write(str(moves))
            child = node.childNode(problem, moves)  # expanded node
            if child.state not in exploredNodes and child not in fringe:
                nodes_generated += 1
                child.depth = node.depth + 1
                if problem.goalState(child.state):
                    # depth = child.depth
                    # while child.parent:
                    # child = child.parent
                    # depth += 1
                    print('Nodes Popped = ', nodes_popped)
                    print('Nodes Expanded = ', nodes_expanded)
                    print('Nodes Generated = ', nodes_generated)
                    print('Max Fringe Size = ', max(max_fringe_size, len(fringe)))
                    print('Solution found at depth = ', child.depth)
                    print('Steps: ')
                    return child
                fringe.append(child)
                max_fringe_size = max(max_fringe_size, len(fringe))
    return None


# Depth First Search
def DFS(problem):
    global node
    fringe = list([node])  # LIFO
    explored = set()
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 1  # Initial node is generated
    max_fringe_size = 1
    depth = 0

    while fringe:
        node = fringe.pop()  # LIFO
        nodes_popped += 1
        if node.state not in explored:
            if flag:
                file.write('Explored Nodes: ')
                file.write(str(explored))
            explored.add(node.state)  # explored node
            nodes_expanded += 1
            depth = node.depth
        for moves in problem.moves(node.state):
            if flag:
                file.write('Move: ')
                file.write(str(moves))
            child = node.childNode(problem, moves)  # expanded node
            if child.state not in explored and child not in fringe:
                nodes_generated += 1
                if problem.goalState(child.state):
                    print('Nodes Popped = ', nodes_popped)
                    print('Nodes Expanded = ', nodes_expanded)
                    print('Nodes Generated = ', nodes_generated)
                    print('Max Fringe Size = ', max(max_fringe_size, len(fringe)))
                    print('Solution found at depth =', depth + 1)
                    print('Steps: ')
                    return child
                fringe.append(child)
                max_fringe_size = max(max_fringe_size, len(fringe))
    return None


# Method to calculate the number of misplaced tiles
def heuristic(state, goal_state):
    misplaced = sum([1 if state[i] != goal_state[i] else 0 for i in range(len(state))])
    return misplaced


# Uniform Cost Search
def UCS(problem, node):
    fringe = []  # Priority queue
    heapq.heappush(fringe, node)  # Adding the initial node to the priority queue
    exploredNodes = set()  # Using set instead of list
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 1
    max_fringe_size = 1

    while fringe:
        node = fringe.pop(fringe.index(min(fringe, key=lambda x: heuristic(x.state, goal1))))
        nodes_popped += 1
        if problem.goalState(node.state):
            total_cost = node.pathCost
            depth = node.depth
            print(f"Nodes Popped: {nodes_popped}")
            print(f"Nodes Expanded: {nodes_expanded}")
            print(f"Nodes Generated: {nodes_generated}")
            print(f"Max Fringe Size: {max_fringe_size}")
            print(f"Solution Found at Depth {depth + 1} with cost {total_cost}")
            print('Steps: ')
            return node
        if node.state not in exploredNodes:
            exploredNodes.add(node.state)  # Explored node
            if flag:
                file.write('Explored Nodes: ')
                file.write(str(exploredNodes))
            nodes_expanded += 1
            for move in problem.moves(node.state):
                if flag:
                    file.write('Move: ')
                    file.write(str(move))
                child = node.childNode(problem, move)  # Expanded node
                child.depth = node.depth + 1
                nodes_generated += 1
                if child.state not in exploredNodes:
                    heapq.heappush(fringe, child)  # Adding the child to the priority queue
                    max_fringe_size = max(max_fringe_size, len(fringe))
                elif child in fringe:
                    for i, frontier_node in enumerate(fringe):
                        if frontier_node == child and child.pathCost < frontier_node.pathCost:
                            fringe[i] = child  # Replacing the frontier node with lower cost child
                            heapq.heapify(fringe)  # Maintaining heap property
    return None


# Depth Limited Search
def DLS(node, problem, limit):
    fringe = list([node])  # LIFO
    explored = list()  # contains the explored statuses
    explored_depth = list()  # contains the depth of the explored statuses
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 1  # Initial node is generated
    max_fringe_size = 1
    while fringe:
        node = fringe.pop()
        nodes_popped += 1
        if node.state not in explored:
            if flag:
                file.write('Explored Nodes: ')
                file.write(str(explored))
            explored.append(node.state)
            explored_depth.append(node.depth)
            nodes_expanded += 1
        if problem.goalState(node.state):
            print('Nodes Popped = ', nodes_popped)
            print('Nodes Expanded = ', nodes_expanded)
            print('Nodes Generated = ', nodes_generated)
            print('Max Fringe Size = ', max_fringe_size)
            print('Solution found at depth = ', node.depth)
            print('Steps: ')
            return node
        else:
            for child in node.expand(problem):
                if child.depth <= limit:  # Current depth does not exceed Limit
                    nodes_generated += 1
                    if child not in fringe:  # if not in fringe
                        if child.state not in explored:  # if not in explored
                            if flag:
                                file.write('Explored Nodes: ')
                                file.write(str(explored))
                            if problem.goalState(child.state):
                                print('Nodes Popped = ', nodes_popped)
                                print('Nodes Expanded = ', nodes_expanded)
                                print('Nodes Generated = ', nodes_generated)
                                print('Max Fringe Size = ', max(max_fringe_size, len(fringe) + 1))
                                print('Solution found at depth = ', child.depth)
                                print('Steps: ')
                                return child
                            else:
                                fringe.append(child)  # push child in fringe
                                max_fringe_size = max(max_fringe_size, len(fringe))
                        elif explored_depth[explored.index(child.state)] > child.depth:
                            explored_depth[explored.index(child.state)] = child.depth
                            if problem.goalState(child.state):
                                print('Nodes Popped = ', nodes_popped)
                                print('Nodes Expanded = ', nodes_expanded)
                                print('Nodes Generated = ', nodes_generated)
                                print('Max Fringe Size = ', max(max_fringe_size, len(fringe) + 1))
                                print('Solution found at depth = ', child.depth)
                                print('Steps: ')
                                return child
                            else:
                                fringe.append(child)  # push child in fringe
                                max_fringe_size = max(max_fringe_size, len(fringe))

                else:
                    break
    return None


# Iterative Deepening Search
def IDS(problem, node):
    depthlimit = 0
    for depthlimit in itertools.count():
        result = DLS(node, problem, limit=depthlimit)
        if result != None:
            break
    return result


# Greedy Search
def Greedy_Search(problem, node):
    # global node
    fringe = list([node])  # Priority queue
    exploredNodes = set()  # Using set instead of list
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 1  # Initial node is generated
    max_fringe_size = 1
    depth = 0
    while fringe:
        node = fringe.pop(fringe.index(min(fringe, key=lambda x: manhattan_distance(x.state))))
        nodes_popped += 1
        if problem.goalState(node.state):
            print('Nodes Popped = ', nodes_popped)
            print('Nodes Expanded = ', nodes_expanded)
            print('Nodes Generated = ', nodes_generated)
            print('Max Fringe Size = ', max(max_fringe_size, len(fringe)))
            print('Solution found at depth: ', node.depth)
            print('Steps: ')
            return node
        if node.state not in exploredNodes:
            exploredNodes.add(node.state)  # explored node
            if flag:
                file.write('Explored Nodes: ')
                file.write(str(exploredNodes))
            nodes_expanded += 1
        for moves in problem.moves(node.state):
            child = node.childNode(problem, moves)  # expanded node
            if flag:
                file.write('Move: ')
                file.write(str(moves))
            if child.state not in exploredNodes and child not in fringe:
                nodes_generated += 1
                child.depth = node.depth + 1
                fringe.append(child)
                max_fringe_size = max(max_fringe_size, len(fringe))
    return None

# A* Search
def AStar(problem, node):
    # global node
    fringe = list([node])  # Priority queue
    exploredNodes = set()  # Using set instead of list
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 1  # Initial node is generated
    max_fringe_size = 1
    depth = 0
    while fringe:
        node = fringe.pop(fringe.index(min(fringe, key=lambda x: heuristic(x.state, goal1) + manhattan_distance(
            x.state))))  # choose the lowest h(n)
        nodes_popped += 1
        if problem.goalState(node.state):
            print('Nodes Popped = ', nodes_popped)
            print('Nodes Expanded = ', nodes_expanded)
            print('Nodes Generated = ', nodes_generated)
            print('Max Fringe Size = ', max(max_fringe_size, len(fringe)))
            print('Solution found at depth: ', node.depth)
            print('Total Cost: ', node.g)  # print the total cost
            print('Steps: ')
            return node
        if node.state not in exploredNodes:
            exploredNodes.add(node.state)  # explored node
            if flag:
                file.write('Explored Nodes: ')
                file.write(str(exploredNodes))
            nodes_expanded += 1
        for moves in problem.moves(node.state):
            if flag:
                file.write('Move: ')
                file.write(str(moves))
            child = node.childNode(problem, moves)  # expanded node
            if child.state not in exploredNodes and child not in fringe:
                nodes_generated += 1
                child.g = node.g + 1  # set the g(n) value of the child node
                child.depth = node.depth + 1
                fringe.append(child)
                max_fringe_size = max(max_fringe_size, len(fringe))
            elif child in fringe and child.g > node.g + 1:
                child.g = node.g + 1  # update the g(n) value if a better path is found
                child.depth = node.depth + 1
    return None


def manhattan_distance(state):
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    goal_dict = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                 4: (1, 0), 5: (1, 1), 6: (1, 2),
                 7: (2, 0), 8: (2, 1), 0: (2, 2)}
    state_dict = {state[i]: (i // 3, i % 3) for i in range(9)}

    distance = 0
    for tile in range(1, 9):
        curr_pos = state_dict[tile]
        goal_pos = goal_dict[tile]
        distance += abs(curr_pos[0] - goal_pos[0]) + abs(curr_pos[1] - goal_pos[1])

    return distance

# Method to read the contents of start and goal file
def read_file(filename):
    numbers = []
    with open(filename, 'r') as f:
        numbers = []
        for line in f:
            if line.strip() == 'END OF FILE':
                break
            numbers += [int(x) for x in line.strip().split()]
    # print(numbers)
    return tuple(numbers)


# **********************************************************************


if __name__ == '__main__':
    # start1 = (2, 3, 6, 1, 0, 7, 4, 8, 5)
    # goal1 = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    # start1 = read_file('start.txt')
    # goal1 = read_file('goal.txt')
    if len(sys.argv) < 4:
        print('Give the command as follows:\n main.py start.txt goal.txt <method> <true/false>')
    start_file = sys.argv[1]
    goal_file = sys.argv[2]
    try:
        algo = sys.argv[3]
        flag = sys.argv[4]
    except:
        algo = 'a*'
        flag = False

    if str(flag).lower() == 'true':
        flag = True
    else:
        flag = False

    start1 = read_file(start_file)
    goal1 = read_file(goal_file)
    problem = EightPuzzle(start=start1, goal=goal1)
    node = Node(problem.start)

    if flag:
        file.write('Command Line Arguments: ')
        file.write(start_file)
        file.write('\t')
        file.write(goal_file)
        file.write('\t')
        file.write(algo)
        file.write('\t')
        file.write(str(flag))
        file.write('\n')
        file.write('Method Selected: ')
        file.write(algo)
        file.write('\n')

    if algo.lower() == 'bfs':
        # working
        result = BFS(problem)
        if result:
            print(result.solution())
        else:
            print('No solution found')
    elif algo.lower() == 'dfs':
        # working
        result = DFS(problem)
        if result:
            print(result.solution())
            file.close()
        else:
            print('No solution found')
    elif algo.lower() == 'ids':
        # working
        result = IDS(problem, node)
        if result:
            print(result.solution())
        else:
            print('No solution found')
    elif algo.lower() == 'dls':
        # working
        depthLimit = int(input('Enter the depth limit: '))
        result = DLS(node, problem, depthLimit)
        if result:
            print(result.solution())
        else:
            print('No solution found')
    elif algo.lower() == 'ucs':
        # working
        result = UCS(problem, node)
        if result:
            print(result.solution())
        else:
            print('No solution found')
    elif algo.lower() == 'greedy':
        # working
        result = Greedy_Search(problem, node)
        if result:
            print(result.solution())
        else:
            print('No solution found')
    else:
        # working
        print('A* Search')
        result = AStar(problem, node)
        if result:
            print(result.solution())
        else:
            print('No solution found')
