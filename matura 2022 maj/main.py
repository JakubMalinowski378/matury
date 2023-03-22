def number_distribution(n):
    factors = []
    i = 2
    while n > 1:
        while n % i == 0:
            factors.append(i)
            n /= i
        i += 1
    return factors


def ex1(data):
    counter = 0
    first_number = None
    for number in data:
        number_string = str(number)
        if number_string[0] == number_string[-1]:
            counter += 1
            if first_number is None:
                first_number = number
    print(counter, first_number)


def ex2(data):
    max_factors = 0
    max_factors_number = None
    max_different_factors = 0
    max_different_factors_number = None
    for number in data:
        factors = number_distribution(number)
        if len(factors) > max_factors:
            max_factors = len(factors)
            max_factors_number = number
        if len(set(factors)) > max_different_factors:
            max_different_factors = len(set(factors))
            max_different_factors_number = number
    print(max_factors_number, max_factors,
          max_different_factors_number, max_different_factors)


def ex3a(data):
    counter = 0
    for x in data:
        for y in data:
            if y % x == 0 and y not in [x]:
                for z in data:
                    if z % y == 0 and z not in [x, y]:
                        print(x, y, z)
                        counter += 1
    print(counter)


def ex3b(data):
    counter = 0
    for u in data:
        for w in data:
            if w % u == 0 and w not in [u]:
                for x in data:
                    if x % w == 0 and x not in [u, w]:
                        for y in data:
                            if y % x == 0 and y not in [u, w, x]:
                                for z in data:
                                    if z % y == 0 and z not in [u, w, x, y]:
                                        print(u, w, x, y, z)
                                        counter += 1
    print(counter)


def main():
    with open('liczby.txt', 'r') as file:
        data = list(map(int, file.readlines()))
        ex1(data)
        ex2(data)
        ex3a(data)
        ex3b(data)


if __name__ == "__main__":
    main()
