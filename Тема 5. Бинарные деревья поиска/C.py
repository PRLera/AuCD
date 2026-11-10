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


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


tree = BST()
numbers = list(map(int, input().split()))
for n in numbers:
    if n == 0:
        break
    tree.insert(n)

print(count_nodes(tree.root))