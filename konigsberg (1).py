def build_konigsberg_graph():
    """
    Builds the graph representation of the Königsberg bridge problem.
    """
    graph = {}
    # Represent the four land masses as vertices (A, B, C, D)
    graph["A"] = ["B", "D", "C"]
    graph["B"] = ["A", "D", "C"]
    graph["C"] = ["A", "B", "D"]
    graph["D"] = ["A", "B", "C"]
    return graph

def is_eulerian_path(graph):
    """
    Checks if a graph has an Eulerian path.
    An Eulerian path exists if at most two vertices have odd degree.
    """
    odd_degree_count = 0
    for vertex in graph:
        if len(graph[vertex]) % 2 != 0:  # Check if the degree is odd
            odd_degree_count += 1
    return odd_degree_count <= 2

# Build the Königsberg graph
konigsberg_graph = build_konigsberg_graph()

# Check if the graph has an Eulerian path
has_eulerian_path = is_eulerian_path(konigsberg_graph)

# Output the result
if has_eulerian_path:
    print("The Königsberg bridge problem has a solution (Eulerian path).")
else:
    print("The Königsberg bridge problem does not have a solution (no Eulerian path).")