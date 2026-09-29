C = float(input())

left = 0
right = C

while right - left > 1e-7:  # Пока разница больше точности
    mid = (left + right) / 2
    if mid * mid + mid ** 0.5 < C:
        left = mid
    else:
        right = mid

print(f"{(left + right) / 2:.10f}")