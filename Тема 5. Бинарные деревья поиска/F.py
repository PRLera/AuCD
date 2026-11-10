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


def leaves_iterative(root):
    """Итеративный симметричный обход, выводим только листья"""
    result = []
    stack = []
    curr = root

    while curr is not None or stack:
        # Идём влево до конца
        while curr is not None:
            stack.append(curr)
            curr = curr.left

        # Берём узел из стека
        curr = stack.pop()

        # Проверяем, является ли узел листом
        if curr.left is None and curr.right is None:
            result.append(curr.data)

        # Переходим к правому поддереву
        curr = curr.right

    return result


# === Читаем ВСЕ числа из всего ввода ===
data = sys.stdin.read().split()
numbers = [int(x) for x in data]

tree = BST()
for n in numbers:
    if n == 0:
        break
    tree.insert(n)

result = leaves_iterative(tree.root)
print('\n'.join(map(str, result)))