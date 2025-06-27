import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        dist, current_node = heapq.heappop(priority_queue)

        if dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

if __name__ == '__main__':
    graph = {
        'A': {'B': 2, 'C': 4},
        'B': {'C': 1, 'D': 5},
        'C': {'D': 2},
        'D': {'E': 3},
        'E': {}
    }
    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)
    print(f"Shortest distances from node {start_node}: {shortest_distances}")
