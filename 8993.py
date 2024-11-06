 
from collections import Counter
a = input()
b = input()
count_a = Counter(a)
count_b = Counter(b)
mümkündür = all(count_b[char] <= count_a[char] for char in count_b)
print("Ok" if mümkündür else "No")