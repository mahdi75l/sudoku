suduku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def show_table():
    counter_row = 0
    for row in suduku:
        counter_column = 0
        row_str = "|"
        for column in row:
            row_str += f" {column}"
            if counter_column in (2, 5, 8):
                row_str += " |"
            counter_column += 1

        print(row_str)
        if counter_row in (2, 5, 8):
            print("-------------------------")
        counter_row += 1


def find_free():
    row = 0
    while row < 9:
        column = 0
        while column < 9:
            if suduku[row][column] == 0:
                return row, column
            column += 1
        row += 1
    return -1, -1


def is_valid(n, row, column):
    i = 0
    while i < 9:
        if suduku[row][i] == n or suduku[i][column] == n:
            return False
        i += 1

    row_fake = int(row / 3) * 3
    column_fake = int(column / 3) * 3


    i = 0
    while i < 3:
        j = 0
        while j < 3:
            if suduku[row_fake + i][column_fake + j] == n:
                return False
            j += 1
        i += 1
    return True


def solve():
    row, column = find_free()

    if row == -1 and column == -1:
        return True

    if not (row == -1 or column == -1):
        i = 1
        while i < 10:
            if is_valid(i, row, column):
                suduku[row][column] = i
                if solve():
                    return True
                suduku[row][column] = 0
            i += 1
    return False


print(solve())
show_table()
