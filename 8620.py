s = input().strip()
maps = {}
for ch in s:
    if '0' <= ch <= '9':
        maps[ch] = maps.get(ch, 0) + 1
fl = len(maps) == 2
for value in maps.values():
    if value != 1 and value != 3:
        fl = False
print("YES" if fl else "NO")