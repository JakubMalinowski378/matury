def is_number_increasing(n: list[int]):
    for i in range(1, len(n)):
        if n[i-1] > n[i]:
            return False
    return True


def ex1(numbers):
    counter = 0
    for number in numbers:
        if number[0] == number[-1]:
            counter += 1
    print(counter)


def ex2(numbers):
    counter = 0
    for number in numbers:
        number_decimal = str(int(number, 8))
        if number_decimal[0] == number_decimal[-1]:
            counter += 1
    print(counter)


def ex3(numbers):
    counter = 0
    min_number_decimal = None
    max_number_decimal = None
    min_number_octal = 0
    max_number_octal = 0
    for number in numbers:
        digits = list(map(int, list(number)))
        if is_number_increasing(digits):
            counter += 1
            value = int(number, 8)
            if min_number_decimal is None or value < min_number_decimal:
                min_number_decimal = value
                min_number_octal = number
            if max_number_decimal is None or value > max_number_decimal:
                max_number_decimal = value
                max_number_octal = number
    print(f"counter: {counter}\nmin number: {min_number_octal}\nmax number: {max_number_octal}")


def main():
    with open("dane.txt", "r") as file:
        numbers = list(map(lambda x: x.strip(), file.readlines()))
    ex1(numbers)
    ex2(numbers)
    ex3(numbers)


if __name__ == "__main__":
    main()
