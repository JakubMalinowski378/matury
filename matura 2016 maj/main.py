def cezar_cipher(word, key):
    result = ""
    key %= 26
    for char in word:
        ascii_number = ord(char)
        if ascii_number + key <= 90:
            result += chr(ascii_number+key)
        else:
            result += chr(ascii_number+key-26)
    return result


def decrypt(word, key):
    key %= 26
    result = ""
    for char in word:
        ascii_number = ord(char)
        if ascii_number - key >= 65:
            result += chr(ascii_number - key)
        else:
            result += chr(ascii_number - key + 26)
    return result


def is_correct(word, cipher):
    key = ord(cipher[0]) - ord(word[0]) if ord(word[0]) <= ord(cipher[0]) else ord(cipher[0]) - ord(word[0]) + 26
    if cezar_cipher(word, key) == cipher:
        return True
    return False


def ex1():
    with open("dane_6_1.txt", "r") as file:
        words = list(map(lambda x: x.strip(), file.readlines()))
    with open("wyniki_6_1.txt", "w") as file:
        for word in words:
            file.write(f"{cezar_cipher(word, 107)}\n")


def ex2():
    with open("dane_6_2.txt", "r") as file:
        data = list(map(lambda x: x.split(), file.readlines()))
        data = list(map(lambda x: (x[0], int(x[1])), data))
    with open("wyniki_6_2.txt", "w") as result:
        for word, key in data:
            result.write(f"{decrypt(word, key)}\n")


def ex3():
    with open("dane_6_3.txt", "r") as file:
        words = list(map(lambda x: x.split(), file.readlines()))
    with open("wyniki_6_3.txt", "w") as result:
        for word, cipher in words:
            if not is_correct(word, cipher):
                result.write(f"{word}\n")


def main():
    ex1()
    ex2()
    ex3()


if __name__ == "__main__":
    main()
