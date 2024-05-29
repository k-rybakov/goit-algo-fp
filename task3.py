import heapq

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_edge(self, u, v, weight):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))  # Якщо граф неорієнтований, додайте цей рядок

    def dijkstra(self, start):
        # Ініціалізація відстаней та мін-купи
        distances = {vertex: float('inf') for vertex in self.adjacency_list}
        distances[start] = 0
        priority_queue = [(0, start)]
        heapq.heapify(priority_queue)
        predecessors = {vertex: None for vertex in self.adjacency_list}

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Якщо знайдена краща відстань, пропустити
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.adjacency_list[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, predecessors

# Приклад використання
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 1)
    
    start_vertex = 'A'
    distances, predecessors = graph.dijkstra(start_vertex)

    print("Відстані від стартової вершини:")
    for vertex, distance in distances.items():
        print(f"Від {start_vertex} до {vertex}: {distance}")

    print("\nПопередники для побудови шляхів:")
    for vertex, predecessor in predecessors.items():
        print(f"Вершина: {vertex}, Попередник: {predecessor}")
