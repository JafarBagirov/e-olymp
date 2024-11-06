 
from collections import Counter
# Parçaların uzunluqlarını daxil edirik
n = int(input())  # Parçaların sayı
lengths = list(map(int, input().split()))  # Hər bir parçanın uzunluqları
# Hər bir uzunluğun neçə dəfə təkrarladığını sayırıq
length_counts = Counter(lengths)
# Mümkün qədər çox kvadrat düzəltmək üçün 4-lük qruplar tapırıq
squares = 0
for length, count in length_counts.items():
    squares += count // 4  # Hər 4 bərabər uzunluq bir kvadrat düzəldir
print(squares)