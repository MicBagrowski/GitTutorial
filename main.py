print('\n')
zakupy = {
    'Jula':'młotek',
    'Społem':'chleb',
    'Gryvan':'lody'
    }

for sklep, towar in zakupy.items():
    print(f"Idę do sklepu {sklep.title()} i kupię {towar.title()}.")

counter = 0
for towar in zakupy:
    counter+=1
print(f"W sumie kupuję {counter} produkty.\n")

