import sys
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, n):
        if self.root is None:
            self.root = Node(n)
            return
        curr = self.root
        while True:
            if n == curr.data:
                return
            elif n < curr.data:
                if curr.left is None:
                    curr.left = Node(n)
                    return
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = Node(n)
                    return
                curr = curr.right


def height_iterative(root):
    if root is None:
        return 0

    queue = deque([(root, 1)])  # (узел, уровень)
    max_level = 0

    while queue:
        node, level = queue.popleft()
        if level > max_level:
            max_level = level
        # если есть левый сосед
        if node.left:
            queue.append((node.left, level + 1))
        # если есть правый сосед
        if node.right:
            queue.append((node.right, level + 1))

    return max_level


data = sys.stdin.read().split()
tree = BST()
for token in data:
    n = int(token)
    if n == 0:
        break
    tree.insert(n)

print(height_iterative(tree.root))