#Program based on Greedy -approach:Prim's Algorithm for minimal spanning tree 
import heapq

def prim(graph):
    
    pq = [(0, 0)]  
    visited = set()
    min_spanning_tree = []

    while pq:
        weight, current_vertex = heapq.heappop(pq)

        if current_vertex not in visited:
            visited.add(current_vertex)
            
            for neighbor, edge_weight in graph[current_vertex]:
                if neighbor not in visited:
                    heapq.heappush(pq, (edge_weight, neighbor))
            
            if current_vertex != 0:  
                min_spanning_tree.append((current_vertex, weight))

    return min_spanning_tree


graph = {
    0: [(1, 2), (2, 4)],
    1: [(0, 2), (2, 1), (3, 7)],
    2: [(0, 4), (1, 1), (3, 5)],
    3: [(1, 7), (2, 5)]
}

result = prim(graph)
print(result)
