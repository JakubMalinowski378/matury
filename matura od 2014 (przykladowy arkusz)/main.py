from itertools import chain
from collections import Counter


def ex1(numbers):
    counter = 0
    for n1, n2 in numbers:
        n1 = sorted(n1)
        n2 = sorted(n2)
        if n1 == n2:
            counter += 1
    print(counter)


def ex2(numbers):
    numbers = dict(Counter(list(map(lambda y: "".join(y), map(lambda x: sorted(x), chain.from_iterable(numbers))))))
    print(max(numbers.values()))


def main():
    with open("dane_anagramy.txt", "r") as file:
        numbers = list(map(lambda x: x.split(), file.readlines()))
    ex1(numbers)
    ex2(numbers)


if __name__ == "__main__":
    main()
