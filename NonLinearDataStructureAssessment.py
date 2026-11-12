from collections import deque


# ==========================================
# 1. BINARY TREE IMPLEMENTATION
# ==========================================
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_tree_bfs(root):
    if not root:
        return

    queue = deque([root])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current.data)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    print("BFS:", " -> ".join(result))


def print_tree_dfs_preorder(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.data)
        print_tree_dfs_preorder(node.left, result)
        print_tree_dfs_preorder(node.right, result)
    return result


# ==========================================
# 2. GRAPH IMPLEMENTATION
# ==========================================
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def print_bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        result = []

        while queue:
            current = queue.popleft()
            result.append(current)

            for neighbor in self.adj_list.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print("BFS:", " -> ".join(result))

    def print_dfs(self, start_vertex):
        visited = set()
        result = []

        def dfs_helper(current):
            visited.add(current)
            result.append(current)
            for neighbor in self.adj_list.get(current, []):
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start_vertex)
        print("DFS:", " -> ".join(result))


# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    print("========================================")
    print(" 1. BINARY TREE TRAVERSALS (MANABAT) ")
    print("========================================")

    # Constructing Binary Tree with subscripted A's
    root = TreeNode("M")
    root.left = TreeNode("A1")
    root.right = TreeNode("N")
    root.left.left = TreeNode("A2")
    root.left.right = New_B = TreeNode("B")  # mapping B
    root.right.left = TreeNode("A3")
    root.right.right = TreeNode("T")

    print_tree_bfs(root)
    dfs_result = print_tree_dfs_preorder(root)
    print("DFS (Preorder):", " -> ".join(dfs_result))
    print()

    print("========================================")
    print(" 2. GRAPH TRAVERSALS (MANABAT) ")
    print("========================================")

    # Constructing Graph
    graph = Graph()
    vertices = ["M", "A1", "N", "A2", "B", "A3", "T"]
    for v in vertices:
        graph.add_vertex(v)

    graph.add_edge("M", "A1")
    graph.add_edge("M", "N")
    graph.add_edge("A1", "A2")
    graph.add_edge("A1", "B")
    graph.add_edge("N", "A3")
    graph.add_edge("N", "T")
    graph.add_edge("B", "A3")
    graph.add_edge("A3", "T")

    graph.print_bfs("M")
    graph.print_dfs("M")
    print("========================================")