import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heapq.heappush(open_list, Node(start, None, 0, heuristic(start, goal)))
    closed_set = set()

    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        closed_set.add(current_node.position)
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            new_row = current_node.position[0] + dr
            new_col = current_node.position[1] + dc
            new_pos = (new_row, new_col)
            if (0 <= new_row < rows and 0 <= new_col < cols and
                grid[new_row][new_col] == 0 and new_pos not in closed_set):
                g_cost = current_node.g + 1
                h_cost = heuristic(new_pos, goal)
                new_node = Node(new_pos, current_node, g_cost, h_cost)
                heapq.heappush(open_list, new_node)
    return None
