import sys
def f(x):
    return x**3 + 2*x*x - 3
for x in sys.stdin:
    x = float(x)
    print(f(x))