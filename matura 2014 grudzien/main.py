def ex1(numbers):
    counter = 0
    current_strike = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            current_strike += 1
        else:
            current_strike = 0
        if current_strike == 3:
            counter += 1
    print(counter)


def ex2(numbers):
    max_jump = None
    min_jump = None
    max_jump_day = None
    min_jump_day = None
    for day, number in enumerate(numbers, start=1):
        if max_jump is None or number > max_jump:
            max_jump = number
            max_jump_day = day
        if min_jump is None or number < min_jump:
            min_jump = number
            min_jump_day = day
    print(f"shortest: {min_jump}, day: {min_jump_day}\nlongest: {max_jump}, day: {max_jump_day}")


def ex3(numbers):
    current_sequence = 0
    longest_sequence = 0
    start_distance = None
    improve = None
    for i in range(1, len(numbers)):
        if current_sequence == 0 and numbers[i-1] < numbers[i]:
            start_distance = numbers[i-1]
            current_sequence = 1
        if numbers[i-1] < numbers[i]:
            current_sequence += 1
        else:
            current_sequence = 0
        if current_sequence > longest_sequence:
            longest_sequence = current_sequence
            improve = numbers[i] - start_distance
    print(longest_sequence, improve)


def main():
    with open("dziennik.txt", "r") as file:
        numbers = list(map(int, file.readlines()))
    ex1(numbers)
    ex2(numbers)
    ex3(numbers)


if __name__ == "__main__":
    main()
