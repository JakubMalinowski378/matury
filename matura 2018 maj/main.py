def is_distance_less_or_equals_10(word):
    for i in range(len(word)):
        for j in range(i + 1, len(word)):
            difference = abs(ord(word[i]) - ord(word[j]))
            if difference > 10:
                return False
    return True


def ex1(signals):
    message = ""
    for i, signal in enumerate(signals, start=1):
        if i % 40 == 0:
            message += signal[9]
    print(message)


def ex2(signals):
    word = ""
    different_letters_count = 0
    for signal in signals:
        if len(set(signal)) > different_letters_count:
            different_letters_count = len(set(signal))
            word = signal
    print(word, different_letters_count)


def ex3(signals):
    for signal in signals:
        if is_distance_less_or_equals_10(signal):
            print(signal)


def main():
    with open("sygnaly.txt", "r") as file:
        signals = list(map(lambda x: x.strip(), file.readlines()))
    print("EX1")
    ex1(signals)
    print("\nEX2")
    ex2(signals)
    print("\nEX3")
    ex3(signals)


if __name__ == "__main__":
    main()
