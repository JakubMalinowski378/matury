def read_board(n):
    n = n.split()
    return list(n[0])


def count_neighbours(board, row, column):
    neighbours = 0
    column_plus_one = column + 1 if column + 1 != len(board[0]) else 0
    row_plus_one = row + 1 if row + 1 != len(board) else 0
    positions = [(row - 1, column), (row_plus_one, column), (row, column - 1), (row, column_plus_one),
                 (row - 1, column - 1), (row - 1, column_plus_one), (row_plus_one, column - 1),
                 (row_plus_one, column_plus_one)]
    for x, y in positions:
        if board[x][y] == "X":
            neighbours += 1
    return neighbours


def next_generation(board):
    new_board = [['.' for _ in range(len(board[0]))] for _ in range(len(board))]
    for row_index, row in enumerate(board):
        for column_index, cell in enumerate(row):
            neighbour_count = count_neighbours(board, row_index, column_index)
            if (cell == "X" and neighbour_count in [2, 3]) or (cell == "." and neighbour_count == 3):
                new_board[row_index][column_index] = "X"
            else:
                new_board[row_index][column_index] = "."
    return new_board


def count_alive_cells(board):
    counter = 0
    for row in board:
        for cell in row:
            if cell == "X":
                counter += 1
    return counter


def ex1(board):
    for _ in range(36):
        board = next_generation(board)
    print(count_neighbours(board, 1, 18))


def ex2(board):
    for _ in range(1):
        board = next_generation(board)
    print(count_alive_cells(board))


def ex3(board):
    cells_arrangement_before = board
    for generation in range(2, 101):
        board = next_generation(board)
        if cells_arrangement_before == board:
            print(f"Generation: {generation}\nAlive cells: {count_alive_cells(board)}")
            break
        cells_arrangement_before = board


def main():
    with open("gra.txt", "r") as file:
        board = list(map(read_board, file.readlines()))
    ex1(board)
    ex2(board)
    ex3(board)


if __name__ == "__main__":
    main()
