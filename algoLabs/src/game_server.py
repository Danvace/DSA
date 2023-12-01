"""
    Client 1 -- 10 -> Router 1 -- 80 -> Router 2 -- 50 -> Server --20 -> Client 3
                    /                   /
                  40               100
                /               /
            Client 2    --->  /

    input file
    6 6   numbers of nodes and connections
    1 2 6  rooms nodes that are clients
    1 3 10    start_node, end_node, latency
    3 4 80
    4 5 50
    5 6 20
    2 3 40
    2 4 100
"""
import heapq


def parse_data_from_file(path):
    with open(path, "r", encoding="UTF-8") as file:
        data = file.readlines()

    number_of_vertexes, number_of_edges = map(int, data[0].split())
    client_nodes = set(map(int, data[1].split()))

    adjacency_list = {node: [] for node in range(1, number_of_vertexes + 1)}

    for i in range(2, number_of_edges + 2):
        start_node, end_node, latency = map(int, data[i].split())
        adjacency_list[start_node].append((end_node, latency))
        adjacency_list[end_node].append((start_node, latency))

    return adjacency_list, client_nodes


def dijkstra(adjacency_list, client_nodes, node_number) -> int:
    distances = {node: float('inf') for node in adjacency_list}
    distances[node_number] = 0

    priority_queue = [(0, node_number)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in adjacency_list[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    shortest_paths = {node: distances[node] for node in client_nodes}

    return max(shortest_paths.values())


def best_server_place(adjacency_list, client_nodes):
    router_nodes = [router for router in adjacency_list.keys() if router not in client_nodes]

    result = []
    for router in router_nodes:
        max_latency = dijkstra(adjacency_list, client_nodes, router)
        result.append((max_latency, router))

    return min(result)
