import sys


def solve():
    # Быстрый ввод всех данных
    data = sys.stdin.buffer.read().split()

    # Строим дерево
    root = None
    for token in data:
        n = int(token)
        if n == 0:
            break
        if root is None:
            root = [n, None, None]  # [data, left, right]
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

    # Итеративный in-order обход
    result = []
    stack = []
    curr = root

    while curr is not None or stack:
        while curr is not None:
            stack.append(curr)
            curr = curr[1]  # идём влево

        curr = stack.pop()
        result.append(str(curr[0]))
        curr = curr[2]  # идём вправо

    sys.stdout.write('\n'.join(result) + '\n')


solve()