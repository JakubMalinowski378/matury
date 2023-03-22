from math import sqrt
from collections import Counter


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def exercise1(data):
    for number in data:
        reflection = int(str(number)[::-1])
        if reflection % 17 == 0:
            print(reflection)


def exercise2(data):
    max_difference = 0
    max_difference_number = 0
    for number in data:
        reflection = int(str(number)[::-1])
        difference = abs(reflection - number)
        if difference > max_difference:
            max_difference = difference
            max_difference_number = number
    print(f"{max_difference_number} {max_difference}")


def exercise3(data):
    for number in data:
        reflection = int(str(number)[::-1])
        if is_prime(reflection) and is_prime(number):
            print(number)


def exercise4(data):
    counter = dict(Counter(data))
    twiceOccurs, thriceOccurs = 0, 0
    uniqueNumbers = len(set(data))
    for value in counter.values():
        if value == 2:
            twiceOccurs += 1
            continue
        if value == 3:
            thriceOccurs += 1
            continue
    print(f"{uniqueNumbers} {twiceOccurs} {thriceOccurs}")


def main():
    with open('liczby.txt', 'r') as file:
        data = file.readlines()
        data = list(map(int, data))
        exercise1(data)
        exercise2(data)
        exercise3(data)
        exercise4(data)


if __name__ == "__main__":
    main()
