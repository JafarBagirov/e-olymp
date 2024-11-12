def iki_quvvet(a, b):
    count = 0
    power = 2

    while power <= b:
        if power >= a:
            count += 1
        power *= 2

    return count

import math
a,b = map(int, input().split())
print(iki_quvvet(a, b))
