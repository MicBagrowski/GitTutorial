print("\nTen program sprawdza, czy tekst jest palindromem\n")
prompt = "Wpisz tekst, który chcesz sprawdzić\ni naciśnij Enter:\n "
prompt +="(Jeśli nie chcesz sprawdzać więcej tekstów, wpisz 'koniec')   \n"


active = True
while active:
    word = input(prompt)

    if word == 'koniec':
        active = False
    else:
        def if_palindrome(word):
            """Sprawdza czy wpisany tekst jest palindromem"""
            word = word.replace(' ','')
            word = word.lower()
            palindrome = word[::-1];
            return True if word == palindrome else False
     
    if (if_palindrome(word)):
        print("Twoje słowo to palindrom\n")
    else:
        print("\nTwoje słowo nie jest palindromem\n")

    if_palindrome(word)
