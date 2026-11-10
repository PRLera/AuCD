import sys


def solve():
    data = sys.stdin.buffer.read().split()

    root = None
    for token in data:
        n = int(token)
        if n == 0:
            break
        if root is None:
            root = [n, None, None]
        else:
            curr = root
            while True:
                if n == curr[0]:
                    break
                elif n < curr[0]:
                    if curr[1] is None:
                        curr[1] = [n, None, None]
                        break
                    curr = curr[1]
                else:
                    if curr[2] is None:
                        curr[2] = [n, None, None]
                        break
                    curr = curr[2]

    if root is None:
        sys.stdout.write("YES\n")
        return

    # Итеративный post-order обход для вычисления высот и проверки баланса
    heights = {}
    stack = [(root, False)]
    balanced = True

    while stack:
        node, visited = stack.pop()
        node_id = id(node)

        if visited:
            left_h = heights.get(id(node[1]), 0) if node[1] else 0
            right_h = heights.get(id(node[2]), 0) if node[2] else 0
            heights[node_id] = 1 + max(left_h, right_h)
            if abs(left_h - right_h) > 1:
                balanced = False
        else:
            stack.append((node, True))
            if node[2] is not None:
                stack.append((node[2], False))
            if node[1] is not None:
                stack.append((node[1], False))

    sys.stdout.write("YES\n" if balanced else "NO\n")


solve()