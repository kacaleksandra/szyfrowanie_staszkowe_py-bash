import save_files


def decode(text: str) -> str:
    # tablice z alfabetem i samogłoskami
    VOWELS = ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u']
    ALPHABET = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó',
                'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']
    # zmienna, do której będzie zapisywany odkodowany tekst
    decoded = ""
    # zmienna iterująca
    i = 0
    while i < len(text):
        # znalezienie indeksu litery w tablicy ALPHABET, a jak nie to -1
        index_alph = ALPHABET.index(text[i].lower()) if text[i].lower() in ALPHABET else -1
        # jeżeli nie istnieje to nie podlega szyfrowaniu
        if index_alph == -1:
            decoded += text[i]
            i += 1
            continue
        # indeks litery po odszyfrowaniu
        orindex = (index_alph - 3) % len(ALPHABET)
        # indeks litery w tablicy VOWELS
        index_vow = VOWELS.index(ALPHABET[orindex]) if ALPHABET[orindex] in VOWELS else -1
        # jeśli oryginalny znak był dużą literą,
        # to zamień znak zwracany przez metodę na dużą literę
        decoded += ALPHABET[orindex].upper() if text[i].isupper() else ALPHABET[orindex]
        # określenie oryginalnej litery i sprawdzenie czy jest to spółgłoska
        if index_vow < 0:
            # jeżeli kolejny znak to nie jest 'o' to znaczy, że w zaszyfrowanym komunikacie jest błąd!
            if i + 1 >= len(text) or text[i + 1] != 'o':
                return "Błędny szyfr!\n"
            # jeżeli jest to spółgłoska to trzeba pominąć kolejną literę, ponieważ jest ona 'o'
            i += 1
        i += 1
    return decoded


def main():
    save_files.save_files(False)


if __name__ == '__main__':
    main()
