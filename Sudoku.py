board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9], ]


def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("                                      ")

        for j in range(len(b[0])):
            if j % 3 == 0:
                print("   ", end="")

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")


def empty(b):  # Finds first empty square
    for i in range(len(b)):
        for j in range(len(b[0])):
            if not b[i][j]:
                return i, j

    return None


def check(b, n, p):  # Checks if number is valid in Column, Row, and Square

    for i in range(len(b)):  # Checking Columns
        if b[i][p[1]] == n and p[0] != i:
            return False

    for i in range(len(b[0])):  # Checking Rows
        if b[p[0]][i] == n and p[1] != i:
            return False

    for i in range((p[0] // 3) * 3, ((p[0] // 3) * 3) + 3):  # Checking Squares
        for j in range((p[1] // 3) * 3, ((p[1] // 3) * 3) + 3):
            if b[i][j] == n and (i, j) != p:
                return False

    return True


def solution(b):
    e = empty(b)
    if e:
        r, c = e
    else:
        return True

    for i in range(1, 10):
        if check(b, i, (r, c)):
            b[r][c] = i

            if solution(b):
                return True

            b[r][c] = 0

    return False


print("Before solution: ")
print_board(board)
solution(board)
print("                              ")
print("After solution: ")
print_board(board)
