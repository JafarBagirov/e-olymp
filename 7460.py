 
import math
n,m,k = map(int, input().split())
oglanlar_otaq = math.ceil(n / k)
qizlar_otaq = math.ceil(m / k)
umumi_otaq = oglanlar_otaq + qizlar_otaq
print(umumi_otaq)