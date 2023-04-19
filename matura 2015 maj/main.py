def ex1(numbers):
    counter = 0
    for number in numbers:
        zeros_count = number.count("0")
        ones_count = len(number) - zeros_count
        if zeros_count > ones_count:
            counter += 1
    print(counter)


def ex2(numbers):
    numbers_divisible_by_2 = 0
    numbers_divisible_by_8 = 0
    for number in numbers:
        if number[-1] == "0":
            numbers_divisible_by_2 += 1
        if number[-3:] == "000":
            numbers_divisible_by_8 += 1
    print(numbers_divisible_by_2, numbers_divisible_by_8)


def ex3(numbers):
    max_value = None
    min_value = None
    max_line = None
    min_line = None
    for index, number in enumerate(numbers, start=1):
        value = int(number, 2)
        if max_value is None or value > max_value:
            max_value = value
            max_line = index
        if min_value is None or value < min_value:
            min_value = value
            min_line = index
    print(f"minValue line: {min_line}\nmaxValue line: {max_line}")


def main():
    with open("liczby.txt", "r") as file:
        numbers = list(map(lambda x: x.strip(), file.readlines()))
    ex1(numbers)
    ex2(numbers)
    ex3(numbers)


if __name__ == "__main__":
    main()
