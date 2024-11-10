def seive_of_eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return is_prime
prime = seive_of_eratosthenes(100000)
a, b = map(int, input().split())
for i in range (a, b + 1):
    if prime[i]: print(i,end=' ')