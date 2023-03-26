from collections import Counter


def prepare_data(data):
    data = data.split()
    code, city, *rest = data
    rest = list(map(int, rest))
    return [code, city, rest]


def exercise1(data):
    data = map(lambda x: x[0], data)
    with open("wynik4_1.txt", "w") as file:
        for code, number in dict(Counter(data)).items():
            file.write(f"{code} {number}\n")


def exercise2(data):
    cities = []
    with open("wynik4_2a.txt", "w") as file:
        for _, city, dimensions in data:
            area = 0
            venues_count = 0
            for i in range(0, len(dimensions), 2):
                if dimensions[i] != 0 and dimensions[i+1] != 0:
                    area += dimensions[i] * dimensions[i+1]
                    venues_count += 1
                else:
                    break
            file.write(f"{city} {area} {venues_count}\n")
            cities.append((city, area))
    with open("wynik4_2b.txt", "w") as file:
        cities.sort(key=lambda x: x[1])
        file.write(f"{cities[-1][0]} {cities[-1][1]}\n")
        file.write(f"{cities[0][0]} {cities[0][1]}\n")


def exercise3(data):
    max_venues_count = None
    max_venues_city = ""
    min_venues_count = None
    min_venues_city = ""
    for _, city, dimensions in data:
        unique_dimensions = set()
        for i in range(0, len(dimensions), 2):
            if dimensions[i] != 0 and dimensions[i + 1] != 0:
                unique_dimensions.add(dimensions[i]*dimensions[i+1])
            else:
                break
        if max_venues_count is None or len(unique_dimensions) > max_venues_count:
            max_venues_count = len(unique_dimensions)
            max_venues_city = city
        if min_venues_count is None or len(unique_dimensions) < min_venues_count:
            min_venues_count = len(unique_dimensions)
            min_venues_city = city
    with open("wynik4_3.txt", "w") as file:
        file.write(f"{max_venues_city} {max_venues_count}\n{min_venues_city} {min_venues_count}\n")


def main():
    with open("galerie.txt", "r") as file:
        data = list(map(prepare_data, file.readlines()))
        exercise1(data)
        exercise2(data)
        exercise3(data)


if __name__ == "__main__":
    main()
