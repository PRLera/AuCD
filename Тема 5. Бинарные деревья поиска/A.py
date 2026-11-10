class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Вставка
    def add(self, n):
        if self.root is None:
            self.root = Node(n)
            return "DONE"

        curr = self.root
        while True:
            if n == curr.data:
                return "ALREADY"
            elif n < curr.data:
                if curr.left is None:
                    curr.left = Node(n)
                    return "DONE"
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = Node(n)
                    return "DONE"
                curr = curr.right

    # Поиск
    def search(self, n):
        curr = self.root
        while curr is not None:
            if n == curr.data:
                return "YES"
            elif n < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return "NO"

    # Поиск максимального узла в поддереве
    def _find_max(self, node):
        while node.right is not None:
            node = node.right
        return node

    # Удаление узла из поддерева (рекурсивно)
    def _delete_node(self, node, n):
        if node is None:
            return None

        if n < node.data:
            node.left = self._delete_node(node.left, n)
        elif n > node.data:
            node.right = self._delete_node(node.right, n)
        else:
            # Нашли узел для удаления
            # Случай 1: нет левого соседа
            if node.left is None:
                return node.right
            # Случай 2: нет правого соседа
            if node.right is None:
                return node.left
            # Случай 3: два соседа — меняем с максимумом левого поддерева
            max_left = self._find_max(node.left)
            node.data = max_left.data
            node.left = self._delete_node(node.left, max_left.data)

        return node

    # Удаление (публичный метод)
    def delete(self, n):
        if self.search(n) == "NO":
            return "CANNOT"
        self.root = self._delete_node(self.root, n)
        return "DONE"

    # Вывод дерева
    def print_tree(self, node, level, result):
        if node is None:
            return
        self.print_tree(node.left, level + 1, result)
        result.append("." * level + str(node.data))
        self.print_tree(node.right, level + 1, result)


# Основная программа
tree = BST()

while True:
    try:
        line = input().split()
    except EOFError:
        break

    if not line:
        continue

    cmd = line[0]

    if cmd == "ADD":
        n = int(line[1])
        print(tree.add(n))
    elif cmd == "DELETE":
        n = int(line[1])
        print(tree.delete(n))
    elif cmd == "SEARCH":
        n = int(line[1])
        print(tree.search(n))
    elif cmd == "PRINTTREE":
        result = []
        tree.print_tree(tree.root, 0, result)
        print('\n'.join(result))