def ex1(data):
    data = list(map(lambda x: [x.strip(), sum(map(int, list(x[3:].strip())))], data))
    maxSum = 0
    maxIds = []
    for id, summedValue in data:
        if summedValue > maxSum:
            maxSum = summedValue
            maxIds = [id]
            continue
        if summedValue == maxSum:
            maxIds.append(id)
    print(maxIds)


def ex2(data):
    for row in data:
        identifier = row[:3]
        number = row[3:-1]
        if identifier == identifier[::-1] or number == number[::-1]:
            print(row.strip())


def ex3(data):
    for row in data:
        controlSumArray = []
        identifier = row[:3]
        controlNumber = int(row[3])
        for letter in identifier:
            controlSumArray.append(ord(letter)-55)
        controlSumArray.extend(list(map(int, list(row[4:].strip()))))
        controlSumArray[0] *= 7
        controlSumArray[1] *= 3
        controlSumArray[3] *= 7
        controlSumArray[4] *= 3
        controlSumArray[6] *= 7
        controlSumArray[7] *= 3
        if sum(controlSumArray) % 10 != controlNumber:
            print(row.strip())


def main():
    with open("identyfikator.txt", 'r') as file:
        data = file.readlines()
        print('1')
        ex1(data)
        print('2')
        ex2(data)
        print('3')
        ex3(data)


if __name__ == "__main__":
    main()
