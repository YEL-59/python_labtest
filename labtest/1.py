alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    encrypted_word = []
    words = ""
    new_text = text.split(" ")
    for _ in range(len(new_text)):
        words = ""
        for letter in new_text[_]:
            position = alphabet.index(letter)
            new_pos = position + shift
            new_letter = alphabet[new_pos]
            words += new_letter
        encrypted_word.append(words)

    print(encrypted_word[0] + " " + encrypted_word[1])


encrypt(text, shift)