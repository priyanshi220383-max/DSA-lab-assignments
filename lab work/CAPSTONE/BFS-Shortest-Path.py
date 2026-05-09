# ============================================
# BFS - DEGREES OF SEPARATION
# ============================================

from collections import deque

# Social graph
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["C"]
}

# -------- BFS FUNCTION --------
def shortest_path(start, end):

    # Queue stores current node and path
    queue = deque([(start, [start])])

    visited = []

    while queue:

        current, path = queue.popleft()

        # Destination found
        if current == end:
            return path

        visited.append(current)

        # Visit neighbours
        for neighbour in graph[current]:

            if neighbour not in visited:
                queue.append((neighbour, path + [neighbour]))

    return "No path found"


# -------- DEMO --------
print("Shortest Path:")
print(shortest_path("A", "E"))