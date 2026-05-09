# ============================================
# DFS - FRIENDS OF FRIENDS
# ============================================

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

# -------- DFS FUNCTION --------
def dfs(user, depth, visited=None):

    if visited is None:
        visited = []

    # Stop if depth becomes negative
    if depth < 0:
        return

    visited.append(user)

    print(user)

    # Visit friends recursively
    for friend in graph[user]:

        if friend not in visited:
            dfs(friend, depth - 1, visited)


# -------- DEMO --------
print("DFS Traversal:")
dfs("A", 2)