import sys


def solve():
    data = sys.stdin.buffer.read().split()

    root = None
    for token in data:
        n = int(token)
        if n == 0:
            break
        if root is None:
            root = [n, 1, None, None]  # [data, count, left, right]
        else:
            curr = root
            while True:
                if n == curr[0]:
                    curr[1] += 1
                    break
                elif n < curr[0]:
                    if curr[2] is None:
                        curr[2] = [n, 1, None, None]
                        break
                    curr = curr[2]
                else:
                    if curr[3] is None:
                        curr[3] = [n, 1, None, None]
                        break
                    curr = curr[3]

    result = []
    stack = []
    curr = root
    while curr is not None or stack:
        while curr is not None:
            stack.append(curr)
            curr = curr[2]
        curr = stack.pop()
        result.append(f"{curr[0]} {curr[1]}")
        curr = curr[3]

    sys.stdout.write('\n'.join(result) + '\n' if result else '')


solve()