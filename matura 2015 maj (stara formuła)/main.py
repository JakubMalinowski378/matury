def count_block(n):
    counter = 1
    for i in range(1, len(n)):
        if n[i-1] != n[i]:
            counter += 1
    return counter


def longest_zero_sequence(n):
    current_sequence = 0
    longest_sequence = 0
    for char in n:
        if char == "0":
            current_sequence += 1
        else:
            current_sequence = 0
        if current_sequence > longest_sequence:
            longest_sequence = current_sequence
    return longest_sequence


def ex1(words: list[str]):
    counter = 0
    for word in words:
        ones_count = word.count("1")
        zeros_count = len(word) - ones_count
        if zeros_count > ones_count:
            counter += 1
    print(counter)


def ex2(words):
    counter = 0
    for word in words:
        if word[0] == "0" and count_block(word) == 2:
            counter += 1
    print(counter)


def ex3(words):
    result = []
    max_zeros_sequence = 0
    for word in words:
        zeros_sequence = longest_zero_sequence(word)
        if zeros_sequence == max_zeros_sequence:
            result.append(word)
        elif zeros_sequence > max_zeros_sequence:
            max_zeros_sequence = zeros_sequence
            result = [word]
    print(max_zeros_sequence, result)


def main():
    with open("slowa.txt", "r") as file:
        words = list(map(lambda x: x.strip(), file.readlines()))
    ex1(words)
    ex2(words)
    ex3(words)


if __name__ == "__main__":
    main()
