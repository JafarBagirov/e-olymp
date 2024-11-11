n = int(input())
l = list(map(int, input().split()))

max_element = max(l)
index = len(l) - 1 - l[::-1].index(max_element)

l[index], l[-1] = l[-1], l[index]

print(*l)
