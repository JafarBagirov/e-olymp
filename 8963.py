n = int(input())
l = list(map(int, input().split()))
m = min(l)
min_elements = [x for x in l if x == m]
other_elements = [x for x in l if x != m]
l = min_elements + other_elements
print(*l)