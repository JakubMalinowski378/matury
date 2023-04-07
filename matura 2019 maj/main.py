from math import factorial, gcd


def sum_factorial_digits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return sum(map(factorial, digits))


def ex1(numbers):
    power_of_three = [3 ** i for i in range(11)]
    counter = 0
    for number in numbers:
        if number in power_of_three:
            counter += 1
    print(counter)


def ex2(numbers):
    for number in numbers:
        if number == sum_factorial_digits(number):
            print(number)


def ex3(numbers):
    current_gcd = None
    length = 0
    start_number = 0
    max_length = 0
    max_start_number = 0
    max_gcd = 0
    number_before = numbers[0]
    for number in numbers:
        if current_gcd is None:
            length = 1
            current_gcd = number
            start_number = number
            continue
        iter_gcd = gcd(current_gcd, number)
        if iter_gcd > 1:
            length += 1
            current_gcd = iter_gcd
        else:
            if length > max_length:
                max_length = length
                max_gcd = current_gcd
                max_start_number = start_number
            length = 2
            current_gcd = gcd(number, number_before)
            start_number = number_before
        number_before = number
    print(max_start_number, max_length, max_gcd)


def main():
    with open("liczby.txt", "r") as file:
        numbers = list(map(int, file.readlines()))
        print("Zadanie 1")
        ex1(numbers)
        print("\nZadanie 2")
        ex2(numbers)
        print("\nZadanie 3")
        ex3(numbers)


if __name__ == "__main__":
    main()
