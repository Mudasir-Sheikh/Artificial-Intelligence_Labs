class Node:
    def _init_(self, state, parent=None, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth

    def _repr_(self):
        return str(self.state)

def depth_limited_search(node, goal, limit, graph):
    if node.state == goal:
        return node
    elif limit == 0:
        return 'cutoff'  # Reached depth limit, cutoff occurred
    else:
        cutoff_occurred = False
        for child_state in graph.get(node.state, []):
            child_node = Node(child_state, node, node.depth + 1)
            result = depth_limited_search(child_node, goal, limit - 1, graph)
            if result == 'cutoff':
                cutoff_occurred = True
        return 'cutoff' if cutoff_occurred else None

def iterative_deepening_search(start, goal, graph):
    depth = 0
    result = depth_limited_search(Node(start), goal, depth, graph)
    while result == 'cutoff':
        depth += 1
        result = depth_limited_search(Node(start), goal, depth, graph)
    return result

def print_solution_path(node):
    path = []
    while node is not None:
        path.append(node.state)
        node = node.parent
    path.reverse()
    print("Solution path:", path)

# Example graph (as a dictionary)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G', 'H'],
    'F': [],
    'G': [],
    'H': []
}

# Get start and goal states from user input
start_state = input("Enter the start state: ")
goal_state = input("Enter the goal state: ")

result = iterative_deepening_search(start_state, goal_state, graph)

if result is not None:
    print_solution_path(result)
else:
    print("No solution found.")