from math import sqrt
from collections import Counter


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_string_increasing(word):
    for i in range(1, len(word)):
        if ord(word[i-1]) >= ord(word[i]):
            return False
    return True


def ex1(words):
    counter = 0
    for word in words:
        ascii_sum = sum(map(ord, list(word)))
        if is_prime(ascii_sum):
            counter += 1
    print(counter)


def ex2(words):
    for word in words:
        if is_string_increasing(word):
            print(word)


def ex3(words):
    counter = dict(Counter(words))
    for key, value in counter.items():
        if value > 1:
            print(key)


def main():
    with open("NAPIS.TXT", "r") as file:
        words = list(map(lambda x: x.strip(), file.readlines()))
    ex1(words)
    print()
    ex2(words)
    print()
    ex3(words)


if __name__ == "__main__":
    main()
