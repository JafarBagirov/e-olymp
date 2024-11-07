n = int(input())
times = []

for _ in range(n):
    h, m, s = map(int, input().split())

    times.append((h * 3600 + m * 60 + s, h, m, s))

times.sort()

for _, h, m, s in times:
    print(h, m, s)
