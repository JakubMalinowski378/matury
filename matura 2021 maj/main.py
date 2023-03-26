from collections import Counter


def ex4(data):
    result = []
    for instruction, letter in data:
        match instruction:
            case "DOPISZ":
                result.append(letter)
            case "ZMIEN":
                result[-1] = letter
            case "PRZESUN":
                try:
                    index = result.index(letter)
                    if letter == "Z":
                        result[index] = "A"
                        continue
                    result[index] = chr(ord(result[index])+1)
                except ValueError:
                    pass
            case "USUN":
                result.pop()
    return "".join(result)


def ex2(data):
    lastCommand = None
    commandStreak = 0
    maxCommand = None
    maxCommandSteak = 0
    for instuction, _ in data:
        if lastCommand is None:
            lastCommand = instuction
            commandStreak += 1
        if instuction != lastCommand:
            lastCommand = instuction
            commandStreak = 1
        else:
            commandStreak += 1
        if commandStreak > maxCommandSteak:
            maxCommandSteak = commandStreak
            maxCommand = instuction
    print(f"{maxCommand} {maxCommandSteak}")


def ex3(data):
    data = list(map(lambda y: y[1], filter(lambda x: x[0] == "DOPISZ", data)))
    counter = dict(Counter(data))
    mostCommonLetter = 0
    letter = ""
    for key, value in counter.items():
        if value > mostCommonLetter:
            mostCommonLetter = value
            letter = key
    print(letter, mostCommonLetter)


def main():
    with open('instrukcje.txt', 'r') as file:
        data = list(map(lambda x: x.split(), file.readlines()))
        print(len(ex4(data)))
        ex2(data)
        ex3(data)
        print(ex4(data))


if __name__ == "__main__":
    main()
