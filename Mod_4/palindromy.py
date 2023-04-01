def is_palindrome(word):
    """Sprawdza czy wpisany tekst jest palindromem"""
    word = [x for x in word.lower() if x.isalnum()]
    reverse_word = word[::-1]
    return word == reverse_word 

def ask_user_for_words_in_loop_and_print_if_word_is_palindrome():
    """to jest przypadek użycia - jeden z pomysłów na wykorzystanie definicji"""
    print("\nTen program sprawdza, czy tekst jest palindromem\n")
    prompt = """Wpisz tekst, który chcesz sprawdzić i naciśnij Enter. Jeśli nie chcesz sprawdzać więcej tekstów, wpisz 'koniec':  
    """
    while True:
        word = input(prompt)

        if word == 'koniec':
            break
        if is_palindrome(word):
            print("Twoje słowo to palindrom\n")
        else:
            print("\nTwoje słowo nie jest palindromem\n")

ask_user_for_words_in_loop_and_print_if_word_is_palindrome()