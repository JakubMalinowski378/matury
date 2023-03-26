from math import sqrt


def prepare_data(row):
    row = row.split()
    return [int(row[0]), row[1].strip()]


def isPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def ex1(data):
    for number, _ in data:
        if number % 2 == 1:
            continue
        for i in range(2, (number//2)+1):
            if isPrime(i) and isPrime(number-i):
                print(f"{number} {i} {number-i}")
                break


def ex2(data):
    for _, string in data:
        currentLength = 0
        maxLength = 0
        currentLetter = None
        maxLetter = None
        for letter in string:
            if currentLetter is None or letter == currentLetter:
                currentLetter = letter
                currentLength += 1
            else:
                currentLetter = letter
                currentLength = 1
            if currentLength > maxLength:
                maxLetter = letter
                maxLength = currentLength
        print(f"{maxLetter*maxLength} {maxLength}")


def ex3(data):
    data = list(filter(lambda x: len(x[1]) == x[0], data))
    data.sort(key=lambda x: (x[0], x[1]))
    print(data[0])


def main():
    with open("pary.txt", "r") as file:
        data = list(map(prepare_data, file.readlines()))
        ex1(data)
        ex2(data)
        ex3(data)


if __name__ == "__main__":
    main()
