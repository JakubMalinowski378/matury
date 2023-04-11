def prepare_numbers(n):
    n = n.strip()
    return n[:-1], int(n[-1])


def ex1(numbers):
    print(len(tuple(filter(lambda x: x[1] == 8, numbers))))


def ex2(numbers):
    print(len(tuple(filter(lambda x: x[1] == 4 and x[0].count("0") == 0, numbers))))


def ex3(numbers):
    print(len(tuple(filter(lambda x: x[1] == 2 and x[0][-1] == "0", numbers))))


def ex4(numbers):
    print(sum(map(lambda y: int(y[0], 8), filter(lambda x: x[1] == 8, numbers))))


def ex5(numbers):
    min_number_decimal = None
    min_code = None
    max_number_decimal = None
    max_code = None
    for number, system in numbers:
        value = int(number, system)
        if min_number_decimal is None or value < min_number_decimal:
            min_number_decimal = value
            min_code = f"{number}{system}"
        if max_number_decimal is None or value > max_number_decimal:
            max_number_decimal = value
            max_code = f"{number}{system}"
    print(f"MinValue {min_code} {min_number_decimal}\nMaxValue {max_code} {max_number_decimal}")


def main():
    with open("liczby.txt", "r") as file:
        numbers = list(map(prepare_numbers, file.readlines()))
    ex1(numbers)
    ex2(numbers)
    ex3(numbers)
    ex4(numbers)
    ex5(numbers)


if __name__ == "__main__":
    main()
