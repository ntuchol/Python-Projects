def build_konigsberg_graph():
    
    graph = {}
    graph["A"] = ["B", "D", "C"]
    graph["B"] = ["A", "D", "C"]
    graph["C"] = ["A", "B", "D"]
    graph["D"] = ["A", "B", "C"]
    return graph

def is_eulerian_path(graph):
    
    odd_degree_count = 0
    for vertex in graph:
        if len(graph[vertex]) % 2 != 0:  # Check if the degree is odd
            odd_degree_count += 1
    return odd_degree_count <= 2

konigsberg_graph = build_konigsberg_graph()

has_eulerian_path = is_eulerian_path(konigsberg_graph)

if has_eulerian_path:
    print("The Königsberg bridge problem has a solution (Eulerian path).")
else:
    print("The Königsberg bridge problem does not have a solution (no Eulerian path).")
