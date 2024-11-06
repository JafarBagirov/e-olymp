setir = input()
setir = setir.replace("-", "").strip()
while "  " in setir:
    setir = setir.replace("  ", " ")

say = len(setir.split())
print(say)