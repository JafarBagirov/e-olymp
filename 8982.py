 
s = input()
indices = []
index = s.find('a')
if index != -1:
    while index != -1:
        indices.append(index)
        index = s.find('a', index + 1)
    print(*indices)
else: print(index)