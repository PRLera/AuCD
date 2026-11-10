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

    result = []
    stack = []
    curr = root
    while curr is not None or stack:
        while curr is not None:
            stack.append(curr)
            curr = curr[1]
        curr = stack.pop()
        has_left = curr[1] is not None
        has_right = curr[2] is not None
        if has_left != has_right:
            result.append(str(curr[0]))
        curr = curr[2]

    if result:
        sys.stdout.write('\n'.join(result) + '\n')


solve()