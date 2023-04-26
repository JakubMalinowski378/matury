def encryption(word, key):
    result = ""
    for letter, key_letter in zip(word, key):
        ascii_code = ord(letter) + (ord(key_letter)-64)
        if ascii_code > 90:
            ascii_code -= 26
        result += chr(ascii_code)
    return result


def decryption(word, key):
    result = ""
    for letter, key_letter in zip(word, key):
        ascii_code = ord(letter) - (ord(key_letter)-64)
        if ascii_code < 65:
            ascii_code += 26
        result += chr(ascii_code)
    return result


def ex1():
    with open("klucze1.txt", "r") as keys_file, open("tj.txt", "r") as words_file:
        words = list(map(lambda x: x.strip(), words_file.readlines()))
        keys = list(map(lambda x: x.strip(), keys_file.readlines()))
    with open("wynik4a.txt", "w") as output_file:
        for key, word in zip(keys, words):
            if len(key) < len(word):
                key = (key*((len(word)//len(key))+1))[0:len(word)]
            output_file.write(f"{encryption(word, key)}\n")


def ex2():
    with open("sz.txt", "r") as encrypted_file, open("klucze2.txt", "r") as keys_file:
        words = list(map(lambda x: x.strip(), encrypted_file.readlines()))
        keys = list(map(lambda x: x.strip(), keys_file.readlines()))
    with open("wynik4b.txt", "w") as output_file:
        for encrypted_word, key in zip(words, keys):
            if len(key) < len(encrypted_word):
                key = (key * ((len(encrypted_word) // len(key)) + 1))[0:len(encrypted_word)]
            output_file.write(f"{decryption(encrypted_word, key)}\n")


def main():
    ex1()
    ex2()


if __name__ == "__main__":
    main()
