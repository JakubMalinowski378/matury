def ex1(numbers):
    max_length = 0
    max_label = ""
    counter = 0
    for number in numbers:
        half_length = len(number)//2
        if number[0:half_length] == number[half_length:]:
            counter += 1
            if len(number) > max_length:
                max_length = len(number)
                max_label = number
    print(counter, max_length, max_label)


def ex2(numbers):
    wrong_number_count = 0
    min_length = None
    for number in numbers:
        for i in range(0, len(number), 4):
            bcd_code = number[i:i+4]
            if int(bcd_code, 2) > 9:
                wrong_number_count += 1
                if min_length is None or len(number) < min_length:
                    min_length = len(number)
                break
    print(wrong_number_count, min_length)


def ex3(numbers):
    max_number_decimal = None
    max_number_binary = None
    for number in numbers:
        number_decimal = int(number, 2)
        if number_decimal <= 65535 and (max_number_decimal is None or number_decimal > max_number_decimal):
            max_number_decimal = number_decimal
            max_number_binary = number
    print(max_number_decimal, max_number_binary)


def main():
    with open("binarne.txt", "r") as file:
        numbers = list(map(lambda x: x.strip(), file.readlines()))
    ex1(numbers)
    ex2(numbers)
    ex3(numbers)


if __name__ == "__main__":
    main()
