# напрямки: вправо, вниз, діагональ вниз, діагональ вгору
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]


def check_winner(board):
    n = 19

    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                continue

            color = board[x][y]

            for d in range(4):
                nx = x
                ny = y
                count = 1

                # рух вперед
                while True:
                    tx = nx + dx[d]
                    ty = ny + dy[d]

                    if 0 <= tx < n and 0 <= ty < n and board[tx][ty] == color:
                        count += 1
                        nx, ny = tx, ty
                    else:
                        break

                if count == 5:
                    # перевірка на не більше 5
                    px = x - dx[d]
                    py = y - dy[d]

                    nx2 = nx + dx[d]
                    ny2 = ny + dy[d]

                    if 0 <= px < n and 0 <= py < n and board[px][py] == color:
                        continue

                    if 0 <= nx2 < n and 0 <= ny2 < n and board[nx2][ny2] == color:
                        continue

                    return color, x + 1, y + 1

    return 0, -1, -1


def main():
    with open("input.txt", "r") as f:
        data = f.read().split()

    t = int(data[0])
    idx = 1

    for _ in range(t):
        board = []

        for _ in range(19):
            row = list(map(int, data[idx:idx+19]))
            idx += 19
            board.append(row)

        winner, x, y = check_winner(board)

        if winner == 0:
            print(0)
        else:
            print(winner)
            print(x, y)


if __name__ == "__main__":
    main()