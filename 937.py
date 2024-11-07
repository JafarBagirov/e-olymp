def calculate_products(l):
    n = len(l)

    left_products = [1] * n

    right_products = [1] * n

    for i in range(1, n):
        left_products[i] = left_products[i - 1] * l[i - 1]

    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * l[i + 1]

    result = [left_products[i] * right_products[i] for i in range(n)]

    print(" ".join(map(str, result)))

n = int(input())
l = list(map(int, input().split()))

calculate_products(l)
