def lower_bound(arr, x):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid

    return left


def upper_bound(arr, x):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid

    return left


n = int(input())
a = list(map(int, input().split()))

a.sort()

m = int(input())
b = list(map(int, input().split()))

for x in b:
    first = lower_bound(a, x)
    last = upper_bound(a, x)

    print(last - first, end=" ")