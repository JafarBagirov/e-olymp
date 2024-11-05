 
N = float(input())
distance = 10
total_distance = 0
day = 0
while total_distance < N:
    day += 1
    total_distance += distance
    distance *= 1.1
print(day)