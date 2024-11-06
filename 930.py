n = input()
s = ""
say = 0
for i in range(10):
    if str(i) not in n:
        say += 1
        s += str(i)+" "
if say == 0:
    print("0")
else:
    print(say)
    print(s)