tests = int(input())
for _ in range(tests):
    n = int(input())
    s = set()
    for _ in range(n):
        s.add(input())
    print(len(s))