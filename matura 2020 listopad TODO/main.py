def GenerateLuckyNumbers(n):
    lucky_numbers = [True for _ in range(n + 1)]
    lucky_numbers[0] = False
    ln = [1]
    for i in range(2, n+1, 2):
        lucky_numbers[i] = False
    j = 2
    removedNumbersCount = -1
    while removedNumbersCount != 0:
        removedNumbersCount = 0
        counter = 0
        for i in range(1, n+1):
            if lucky_numbers[i]:
                counter += 1
            if counter % j == 0:
                lucky_numbers[i] = False
                removedNumbersCount += 1
        for i in range(1, n+1):
            if lucky_numbers[i] and i not in ln:
                ln.append(i)
                j = i
                break
    print(lucky_numbers)
    print(ln)


def main():
    with open("dane.txt", "r") as file:
        data = list(map(int, file.readlines()))
        # lucky_numbers = GenerateLuckyNumbers(10000)
        GenerateLuckyNumbers(100)


if __name__ == "__main__":
    main()
