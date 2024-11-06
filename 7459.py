 
n = int(input())
if n < 0:
    n = -n
teklik = n % 10
yuzluk = (n // 100) % 10
onminlik = n // 10000
print(teklik * yuzluk * onminlik)