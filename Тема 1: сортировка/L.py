distances = list(map(int, input().split()))
tariffs = list(map(int, input().split()))

distances.sort(reverse=True)
tariffs.sort()

print(sum(d * t for d, t in zip(distances, tariffs)))