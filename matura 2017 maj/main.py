from itertools import chain


def prepare_data(n):
    n = n.split()
    return list(map(int, n))


def ex1(pixels):
    flatten_list = list(chain.from_iterable(pixels))
    print(max(flatten_list), min(flatten_list))


def ex2(pixels):
    counter = 0
    for pixel in pixels:
        left_side = pixel[:160]
        right_side = pixel[160::]
        if left_side != right_side[::-1]:
            counter += 1
    print(counter)


def ex3(pixels, columns=320, rows=200):
    counter = 0
    points = []
    for row in range(rows):
        for column in range(columns):
            pixel = pixels[row][column]
            if row+1 != rows:
                pixel_under = pixels[row+1][column]
                if abs(pixel_under - pixel) > 128:
                    if (row+1, column) not in points:
                        counter += 1
                        points.append((row+1, column))
                    if (row, column) not in points:
                        points.append((row, column))
                        counter += 1
            if column+1 != columns:
                pixel_next_to = pixels[row][column+1]
                if abs(pixel_next_to - pixel) > 128:
                    if (row, column+1) not in points:
                        counter += 1
                        points.append((row, column+1))
                    if (row, column) not in points:
                        counter += 1
                        points.append((row, column))
    print(counter)


def ex4(pixels, columns=320, rows=200):
    longest_sequence = 0
    for column in range(columns):
        column_sequence = []
        for row in range(rows):
            column_sequence.append(pixels[row][column])
        current_counter = 0
        current_number = -1
        for number in column_sequence:
            if number != current_number:
                current_counter = 1
                current_number = number
                continue
            else:
                current_counter += 1
            if current_counter > longest_sequence:
                longest_sequence = current_counter
    print(longest_sequence)


def main():
    with open("dane.txt", "r") as file:
        pixels = list(map(prepare_data, file.readlines()))
    ex1(pixels)
    ex2(pixels)
    ex3(pixels)
    ex4(pixels)


if __name__ == "__main__":
    main()
