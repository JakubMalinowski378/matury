from math import sqrt


def sum_digits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return sum(digits)


def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def ex1(numbers):
    for number in numbers:
        if 100 <= number <= 5000 and is_prime(number):
            print(number)


def ex2(prime_numbers):
    for prime_number in prime_numbers:
        reversed_number = int(str(prime_number)[::-1])
        if is_prime(reversed_number):
            print(prime_number)


def ex3(prime_numbers):
    counter = 0
    for prime_number in prime_numbers:
        while prime_number > 9:
            prime_number = sum_digits(prime_number)
        if prime_number == 1:
            counter += 1
    print(counter)


def main():
    with open("pierwsze.txt", 'r') as file:
        prime_numbers = list(map(int, file.readlines()))
    with open("liczby.txt", "r") as file2:
        numbers = list(map(int, file2.readlines()))
    print("zadanie 1")
    ex1(numbers)
    print("\nzadanie 2")
    ex2(prime_numbers)
    print("\nzadanie 3")
    ex3(prime_numbers)


if __name__ == "__main__":
    main()
