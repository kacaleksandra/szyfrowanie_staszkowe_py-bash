import save_files


def encode(text: str) -> str:
    VOWELS = ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u']
    ALPHABET = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó',
                'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']
    encoded = ""
    for i in range(len(text)):
        index_alph = ALPHABET.index(text[i].lower()) if text[i].lower() in ALPHABET else -1
        if index_alph == -1:
            encoded += text[i]
            continue
        index_vow = VOWELS.index(text[i].lower()) if text[i].lower() in VOWELS else -1
        encoded += ALPHABET[(index_alph + 3) % len(ALPHABET)]
        if text[i].isupper():
            encoded = encoded[:-1] + ALPHABET[(index_alph + 3) % len(ALPHABET)].upper()
        if index_vow < 0:
            encoded += 'o'
    return encoded


def main():
    save_files.save_files(True)


if __name__ == "__main__":
    main()
