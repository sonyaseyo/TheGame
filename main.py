# константи
BOARD_SIZE = 19
WIN_LENGTH = 5

# напрямки: вправо, вниз, діагональ вниз, діагональ вгору dx = [0, 1, 1, -1]
DIRECTIONS = [
    (0, 1),
    (1, 0),
    (1, 1),
    (-1, 1),
]


def read_boards_from_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    # прибираємо порожні рядки
    lines = [line.strip() for line in lines if line.strip()]

    if not lines:
        raise ValueError("Empty input file")

    # читаємо кількість тестів
    try:
        t = int(lines[0])
    except ValueError:
        raise ValueError("First line must be an integer (number of test cases)")

    boards = []
    current_line = 1

    for test_index in range(t):
        board = []

        for row_index in range(BOARD_SIZE):
            if current_line >= len(lines):
                raise ValueError(f"Not enough rows for board {test_index + 1}")

            row_str = lines[current_line]
            current_line += 1

            row_values = row_str.split()

            # 🔴 ключова перевірка
            if len(row_values) != BOARD_SIZE:
                raise ValueError(
                    f"Board {test_index + 1}, row {row_index + 1}: "
                    f"expected {BOARD_SIZE} values, got {len(row_values)}"
                )

            try:
                row = list(map(int, row_values))
            except ValueError:
                raise ValueError(
                    f"Board {test_index + 1}, row {row_index + 1}: invalid number"
                )

            board.append(row)

        boards.append(board)

    if current_line != len(lines):
        raise ValueError("Extra data after last board")

    return boards


def is_exact_five(board, start_row, start_col, end_row, end_col, direction, color):
    dx, dy = direction

    prev_row = start_row - dx
    prev_col = start_col - dy

    next_row = end_row + dx
    next_col = end_col + dy

    if 0 <= prev_row < BOARD_SIZE and 0 <= prev_col < BOARD_SIZE:
        if board[prev_row][prev_col] == color:
            return False

    if 0 <= next_row < BOARD_SIZE and 0 <= next_col < BOARD_SIZE:
        if board[next_row][next_col] == color:
            return False

    return True


def check_winner(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 0:
                continue

            color = board[row][col]

            for direction in DIRECTIONS:
                dx, dy = direction

                current_row = row
                current_col = col
                count = 1

                # рух вперед
                while True:
                    next_row = current_row + dx
                    next_col = current_col + dy

                    if (
                        0 <= next_row < BOARD_SIZE
                        and 0 <= next_col < BOARD_SIZE
                        and board[next_row][next_col] == color
                    ):
                        count += 1
                        current_row, current_col = next_row, next_col
                    else:
                        break

                if count == WIN_LENGTH:
                    if is_exact_five(
                        board,
                        row,
                        col,
                        current_row,
                        current_col,
                        direction,
                        color,
                    ):
                        return color, row + 1, col + 1

    return 0, -1, -1


def main():
    boards = read_boards_from_file("input.txt")

    for board in boards:
        winner, x, y = check_winner(board)

        if winner == 0:
            print(0)
        else:
            print(winner)
            print(x, y)


if __name__ == "__main__":
    main()