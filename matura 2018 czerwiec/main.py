def prepare_data(x):
    x = x.split()
    return list(map(int, x))


def ex1(sequence1, sequence2):
    counter = 0
    for seq1, seq2 in zip(sequence1, sequence2):
        if seq1[-1] == seq2[-1]:
            counter += 1
    print(counter)


def ex2(sequence1, sequence2):
    counter = 0
    for seq1, seq2 in zip(sequence1, sequence2):
        sequence1_odds_number_count = len(list(filter(lambda x: x % 2 == 0, seq1)))
        sequence2_odds_number_count = len(list(filter(lambda x: x % 2 == 0, seq2)))
        if sequence1_odds_number_count == 5 and sequence2_odds_number_count == 5:
            counter += 1
    print(counter)


def ex3(sequence1, sequence2):
    counter = 0
    for row, (seq1, seq2) in enumerate(zip(sequence1, sequence2), start=1):
        if set(seq1) == set(seq2):
            counter += 1
            print(row)
    print(f"liczba ciągów: {counter}")


def ex4(sequence1, sequence2):
    with open("wynik4_4.txt", "w") as result_file:
        for seq1, seq2 in zip(sequence1, sequence2):
            sequence3 = []
            i, j = 0, 0
            while i < 10 and j < 10:
                if seq1[i] <= seq2[j]:
                    sequence3.append(seq1[i])
                    i += 1
                    continue
                sequence3.append(seq2[j])
                j += 1
            if i < 10:
                sequence3.extend(seq1[i:])
            if j < 10:
                sequence3.extend(seq2[j:])
            sequence3 = list(map(str, sequence3))
            result_file.write(f"{' '.join(sequence3)}\n")


def main():
    with open("dane1.txt", "r") as file1:
        sequence1 = list(map(prepare_data, file1.readlines()))
    with open("dane2.txt", "r") as file2:
        sequence2 = list(map(prepare_data, file2.readlines()))
    ex1(sequence1, sequence2)
    ex2(sequence1, sequence2)
    ex3(sequence1, sequence2)
    ex4(sequence1, sequence2)


if __name__ == "__main__":
    main()
