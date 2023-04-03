from math import sqrt


def sum_square_digits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return sum(map(lambda x: x ** 2, digits))


def is_happy(n):
    numbers = set()
    numbers.add(n)
    while True:
        sum_sqare = sum_square_digits(n)
        if sum_sqare == 1:
            numbers.add(1)
            return True, numbers
        if sum_sqare in numbers:
            return False, None
        numbers.add(sum_sqare)
        n = sum_sqare


def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def ex1():
    max_factors = 0
    numbers = []
    for i in range(1, 1000):
        happy, factors = is_happy(i)
        if happy:
            if len(factors) > max_factors:
                max_factors = len(factors)
                numbers = [i]
            if len(factors) == max_factors:
                numbers.append(i)
    print(f"{max_factors}\n{numbers}")


def ex2(data):
    counter = 0
    for number in data:
        happy, factors = is_happy(number)
        if happy:
            counter += 1
    print(counter)


def ex3(data):
    lucky_number_start = None
    length = 0
    max_lucky_number_start = None
    max_lucky_number_end = None
    max_length = 0
    for i, number in enumerate(data):
        happy, _ = is_happy(number)
        if length == 0:
            lucky_number_start = number
        if happy:
            length += 1
        elif length == max_length:
            max_lucky_number_end = data[i-1]
            length = 0
        else:
            length = 0
        if length > max_length:
            max_lucky_number_start = lucky_number_start
            max_length = length
    print(max_length, max_lucky_number_start, max_lucky_number_end)


def ex4(data):
    counter = 0
    for number in data:
        happy, _ = is_happy(number)
        if happy and is_prime(number):
            counter += 1
    print(counter)


def main():
    with open("liczby.txt", 'r') as file:
        data = list(map(int, file.readlines()))
        ex1()
        ex2(data)
        ex3(data)
        ex4(data)


if __name__ == "__main__":
    main()
