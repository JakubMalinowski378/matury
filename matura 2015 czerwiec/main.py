codes = {
    "start": "11011010",
    "stop": "11010110",
    "0": "10101110111010",
    "1": "11101010101110",
    "2": "10111010101110",
    "3": "11101110101010",
    "4": "10101110101110",
    "5": "11101011101010",
    "6": "10111011101010",
    "7": "10101011101110",
    "8": "11101010111010",
    "9": "10111010111010"
}


def count_control_sum(n):
    even_postions_sum = 0
    odd_positions_sum = 0
    n = n[::-1]
    for i, number in enumerate(n):
        if i % 2 == 0:
            even_postions_sum += int(number)
        else:
            odd_positions_sum += int(number)
    return even_postions_sum, odd_positions_sum


def create_code(n, control_sum):
    result = codes["start"]
    for digit in n:
        result += codes[digit]
    result += codes[str(control_sum)]
    result += codes["stop"]
    return result


def ex1(codes_input):
    with open("kody1.txt", "w") as output:
        for code in codes_input:
            even_sum, odd_sum = count_control_sum(code)
            output.write(f"{even_sum} {odd_sum}\n")


def ex2(codes_input):
    with open("kody2.txt", "w") as output:
        for code in codes_input:
            even_sum, odd_sum = count_control_sum(code)
            result = (10 - (3 * even_sum + odd_sum) % 10) % 10
            output.write(f"{codes[str(result)]} {result}\n")


def ex3(codes_input):
    with open("kody3.txt", "w") as output:
        for code in codes_input:
            even_sum, odd_sum = count_control_sum(code)
            control_sum = (10 - (3 * even_sum + odd_sum) % 10) % 10
            output.write(f"{create_code(code, control_sum)}\n")


def main():
    with open("kody.txt", "r") as file:
        codes_input = list(map(lambda x: x.strip(), file.readlines()))
    ex1(codes_input)
    ex2(codes_input)
    ex3(codes_input)


if __name__ == "__main__":
    main()
