setir = input()
sum_ = 0
mul = 1
for c in setir:
    n = int(c)
    sum_ += n
    mul *= n
if sum_ != 0:
    result = mul / sum_
else:
    result = 0
print(f"{result:.3f}")