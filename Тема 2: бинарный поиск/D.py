def f(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d

a, b, c, d = map(int, input().split())
left = -10000.0
right = 10000.0

# Бинарный поиск
for i in range(100):
    mid = (left + right) / 2.0

    # f(mid) и f(left) одного знака,то корень правее
    if f(mid, a, b, c, d) * f(left, a, b, c, d) > 0:
        left = mid
    else:
        right = mid

print(f"{(left + right) / 2.0:.15f}")