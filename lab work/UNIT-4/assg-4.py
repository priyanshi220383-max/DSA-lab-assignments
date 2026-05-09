# ============================================
# BINARY SEARCH TREE (BST)
# ============================================

# Node class for BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# BST class
class BST:
    def __init__(self):
        self.root = None

    # -------- INSERT --------
    def insert(self, value):
        self.root = self.insert_node(self.root, value)

    def insert_node(self, root, value):

        # If tree is empty
        if root is None:
            return Node(value)

        # Insert in left subtree
        if value < root.value:
            root.left = self.insert_node(root.left, value)

        # Insert in right subtree
        else:
            root.right = self.insert_node(root.right, value)

        return root

    # -------- SEARCH --------
    def search(self, root, key):

        # Value found or tree empty
        if root is None or root.value == key:
            return root

        # Search left subtree
        if key < root.value:
            return self.search(root.left, key)

        # Search right subtree
        return self.search(root.right, key)

    # -------- INORDER TRAVERSAL --------
    def inorder(self, root):

        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)

    # -------- DELETE --------
    def delete(self, root, key):

        if root is None:
            return root

        # Go to left subtree
        if key < root.value:
            root.left = self.delete(root.left, key)

        # Go to right subtree
        elif key > root.value:
            root.right = self.delete(root.right, key)

        else:
            # Node with one child or no child
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Node with two children
            temp = self.minimum_value(root.right)

            root.value = temp.value

            root.right = self.delete(root.right, temp.value)

        return root

    # Find minimum value node
    def minimum_value(self, node):

        current = node

        while current.left is not None:
            current = current.left

        return current


# ============================================
# BST DEMONSTRATION
# ============================================

print("===== BINARY SEARCH TREE =====")

bst = BST()

values = [50, 30, 70, 20, 40, 60, 80]

# Insert elements
for v in values:
    bst.insert(v)

print("Inorder Traversal:")
bst.inorder(bst.root)

# Search element
key = 40

result = bst.search(bst.root, key)

if result:
    print("\nElement", key, "found")
else:
    print("\nElement not found")

# Delete element
bst.root = bst.delete(bst.root, 30)

print("Inorder after deletion:")
bst.inorder(bst.root)

print("\n")


# ============================================
# GRAPH USING ADJACENCY LIST
# ============================================

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    # Add edge with weight
    def add_edge(self, u, v, weight):

        if u not in self.graph:
            self.graph[u] = []

        self.graph[u].append((v, weight))

    # -------- BFS --------
    def bfs(self, start):

        visited = set()
        queue = deque([start])

        visited.add(start)

        print("BFS Traversal:")

        while queue:

            node = queue.popleft()

            print(node, end=" ")

            for neighbour, weight in self.graph.get(node, []):

                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

    # -------- DFS --------
    def dfs(self, start, visited=None):

        if visited is None:
            visited = set()
            print("\nDFS Traversal:")

        visited.add(start)

        print(start, end=" ")

        for neighbour, weight in self.graph.get(start, []):

            if neighbour not in visited:
                self.dfs(neighbour, visited)


# ============================================
# GRAPH DEMONSTRATION
# ============================================

print("\n===== GRAPH USING ADJACENCY LIST =====")

g = Graph()

# Directed weighted edges
g.add_edge("A", "B", 5)
g.add_edge("A", "C", 3)
g.add_edge("B", "D", 2)
g.add_edge("C", "D", 4)
g.add_edge("D", "E", 1)

# Perform BFS and DFS
g.bfs("A")
g.dfs("A")

print("\n")


# ============================================
# HASH TABLE WITH SEPARATE CHAINING
# ============================================

class HashTable:

    def __init__(self, size):
        self.size = size

        # Create empty buckets
        self.table = [[] for _ in range(size)]

    # Hash function
    def hash_function(self, key):
        return key % self.size

    # -------- INSERT --------
    def insert(self, key, value):

        index = self.hash_function(key)

        # Append key-value pair
        self.table[index].append((key, value))

    # -------- SEARCH --------
    def search(self, key):

        index = self.hash_function(key)

        for k, v in self.table[index]:

            if k == key:
                return v

        return "Key Not Found"

    # -------- DELETE --------
    def delete(self, key):

        index = self.hash_function(key)

        for i, (k, v) in enumerate(self.table[index]):

            if k == key:
                self.table[index].pop(i)
                return "Key Deleted"

        return "Key Not Found"

    # Display table
    def display(self):

        print("\nHash Table:")

        for i, bucket in enumerate(self.table):
            print(i, "->", bucket)


# ============================================
# HASH TABLE DEMONSTRATION
# ============================================

print("===== HASH TABLE =====")

ht = HashTable(5)

# Insert elements
ht.insert(10, "Apple")
ht.insert(15, "Banana")
ht.insert(20, "Mango")

# Collision example
# 10, 15, 20 all give same index when size = 5
ht.display()

# Search element
print("\nSearch Key 15:")
print(ht.search(15))

# Delete element
print("\nDelete Key 15:")
print(ht.delete(15))

# Display after deletion
ht.display()