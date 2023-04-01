print('Zadanie 1:\n')
liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(liczby)

sześciany = [liczba**3 for liczba in liczby]
print(f"\nSześciany:\n{sześciany}")

niepodzielne_2 = [liczba for liczba in liczby if liczba % 2 != 0]
print(f"\nNieodzielne przez 2:\n{niepodzielne_2}")

podzielne_5 = []
for liczba in range (101):
  if liczba % 5 == 0:
    podzielne_5.append(liczba)
print(f"\nLiczby podzielne przez 5 z zakresu 0 - 100:\n {podzielne_5}\n")

potega_3 = [liczba**3 for liczba in podzielne_5]
print(f"Sześciany tych liczb:\n {potega_3}")



print("\n\nZadanie 2:")
liczby = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
print(f"Lista przed sortowaniem:\n{liczby}")

liczby.sort()
print(f"Lista po sortowaniu:\n{liczby}")

print(f"Tylko zera:\n{liczby[:10]}")

print(f"Tylko liczby:\n{liczby[10:14]}")


