def ex1(data):
    digit_counter = 0
    for line in data:
        for char in line:
            if char.isdigit():
                digit_counter += 1
    print(digit_counter)


def ex2(data):
    password = ""
    position = 0
    for i, line in enumerate(data, start=1):
        if i % 20 == 0:
            password += line[position]
            position += 1
    print(password)


def ex3(data):
    password = ""
    for line in data:
        line = line.strip()
        first_option = line[-1]+line
        if first_option == first_option[::-1]:
            password += first_option[25]
            continue
        second_option = line + line[0]
        if second_option == second_option[::-1]:
            password += second_option[25]
    print(password)


def ex4(data):
    password = ""
    for line in data:
        # 0 - 48, 9 - 57 ASCII
        numbers = list(filter(lambda x: 48 <= ord(x) <= 57, line))
        for i in range(0, len(numbers) - 1, 2):
            number = int(numbers[i] + numbers[i+1])
            if 65 <= number <= 90:
                password += chr(number)
            if len(password) >= 3 and password[-3:] == "XXX":
                break
    print(password)


def main():
    with open('napisy.txt', 'r') as file:
        data = file.readlines()
        ex1(data)
        ex2(data)
        ex3(data)
        ex4(data)


if __name__ == "__main__":
    main()
