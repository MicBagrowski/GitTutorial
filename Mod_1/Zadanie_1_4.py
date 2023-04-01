print("NR 1")
for star1 in range(5):
  for star2 in range(5):
    print("* * * * * * * * * * ")
    print(" * * * * * * * * *")
  break

print("\nNR 2")

tekst = "**"
for i in range(4):
  for j in range(2):
    print(tekst)
  tekst = tekst + "**"


print("\nNR 3")
gwiazdki = 6
for i in range(6):
  print("*" * gwiazdki)
  gwiazdki = gwiazdki - 1