data = list(map(int, input().split()))
n = data[0]
a = data[1:]

destroyed = 0

while True:
    found = False
    i = 0
    while i < len(a):
        j = i
        while j < len(a) and a[j] == a[i]:
            j += 1
        if j - i >= 3:
            destroyed += j - i
            a = a[:i] + a[j:]
            found = True
            break
        i = j
    if not found:
        break

print(destroyed)