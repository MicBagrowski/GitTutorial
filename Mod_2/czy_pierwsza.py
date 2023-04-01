print('\nZadanie 2:\n') 
liczby = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21] 
liczby_pierwsze = []

for liczba in liczby:
    czy_pierwsza = True
    
    if liczba == 1:
        czy_pierwsza = False

    for dzielnik in range(2, liczba):
        if liczba % dzielnik == 0:
            czy_pierwsza == False
            break

    if czy_pierwsza:
        liczby_pierwsze.append(liczba)

print(liczby_pierwsze)

# lub:

liczby = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21] 
liczby_pierwsze = []

for liczba in liczby:
    if liczba == 1: continue
    for dzielnik in range(2, liczba):
        if liczba % dzielnik == 0:
            break
    else:
        liczby_pierwsze.append(liczba)


print(liczby_pierwsze)