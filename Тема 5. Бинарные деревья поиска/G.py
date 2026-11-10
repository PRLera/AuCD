import sys

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

def find_branches(node, result):
    """Итеративный обход, выводим узлы с двумя детьми"""
    if node is None:
        return
    stack = []
    curr = node
    while curr is not None or stack:
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        # Проверяем: есть ли оба ребёнка
        if curr.left is not None and curr.right is not None:
            result.append(curr.data)
        curr = curr.right

data = sys.stdin.read().split()
tree = BST()
for token in data:
    n = int(token)
    if n == 0:
        break
    tree.insert(n)

result = []
find_branches(tree.root, result)
print('\n'.join(map(str, result)))