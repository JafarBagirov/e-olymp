s = []
while True:
    try:
        a, b, c = map(float, input().split())
        s.append(a + b + c)
    except EOFError:
        break

for i in s:
    print(f"{i:.4f}")