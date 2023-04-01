# Lista zakupów

print('\n1. Lista zakupów:')
zakupy = {
    'Jula':'młotek',
    'Społem':'chleb',
    'Cukiernia':'lody'
    }

for sklep, towar in zakupy.items():
    print(f"Idę do sklepu {sklep.title()} i kupię {towar.title()}.")

counter = 0
for towar in zakupy:
    counter+=1
print(f"W sumie kupuję {counter} produkty.\n")

print('\n2. Liczby podzielne przez 5:')

podzielne_5 = []
for liczba in range (101):
  if liczba % 5 == 0:
    podzielne_5.append(liczba)
print(f"\nLiczby podzielne przez 5 z zakresu 0 - 100:\n {podzielne_5}\n")

potega_3 = [liczba**3 for liczba in podzielne_5]
print(f"Sześciany tych liczb:\n {potega_3}\n")