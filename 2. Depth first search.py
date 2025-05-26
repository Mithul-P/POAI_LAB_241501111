def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == goal:
        return path

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path[:])
            if result:
                return result

    return None

def input_graph():
    graph = {}
    n = int(input("Enter number of nodes: "))
    for _ in range(n):
        node = input("Enter node label: ")
        neighbors = input(f"Enter neighbors of {node} separated by spaces (or blank if none): ").split()
        graph[node] = neighbors
    return graph

if __name__ == "__main__":
    warehouse_graph = input_graph()
    start_node = input("Enter start node: ")
    goal_node = input("Enter goal node: ")
    path_found = dfs(warehouse_graph, start_node, goal_node)

    if path_found:
        print(f"DFS Path from {start_node} to {goal_node}: {path_found}")
    else:
        print(f"No path found from {start_node} to {goal_node}.")

