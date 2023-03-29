def ex1(data):
    max_difference = None
    min_difference = None
    for i in range(1, len(data)):
        difference = abs(data[i] - data[i-1])
        if max_difference is None or difference > max_difference:
            max_difference = difference
        if min_difference is None or difference < min_difference:
            min_difference = difference
    print(min_difference, max_difference)


def ex2(data):
    length = 0
    first_number = data[0]
    last_number = 0
    difference = abs(data[0] - data[1])

    max_length = 0
    max_first_number = 0
    max_last_number = 0
    for i in range(1, len(data)):
        if abs(data[i] - data[i-1]) == difference:
            length += 1
        else:
            last_number = data[i-1]
            length += 1
            if length > max_length:
                max_first_number = first_number
                max_last_number = last_number
                max_length = length
            difference = abs(data[i] - data[i-1])
            length = 1
            first_number = data[i-1]
    print(max_length, max_first_number, max_last_number)


def ex3(data):
    counter = {}
    for i in range(1, len(data)):
        difference = abs(data[i-1] - data[i])
        if counter.__contains__(difference):
            counter[difference] += 1
        else:
            counter[difference] = 1
    number, number_of_occurrences = max(counter.items(), key=lambda x: x[1])
    print(number, number_of_occurrences)


def main():
    with open("dane4.txt") as file:
        data = list(map(int, file.readlines()))
        ex1(data)
        ex2(data)
        ex3(data)


if __name__ == "__main__":
    main()
