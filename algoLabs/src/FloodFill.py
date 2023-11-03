def flood_fill(matrix, x, y, target_color, replacement_color):
    row_len = len(matrix)
    col_len = len(matrix[0])
    if x < 0 or x >= row_len or y < 0 or y >= col_len:
        return

    if matrix[x][y] != target_color or matrix[x][y] == replacement_color:  # Check this if it works
        return

    matrix[x][y] = replacement_color

    flood_fill(matrix, x + 1, y, target_color, replacement_color)
    flood_fill(matrix, x - 1, y, target_color, replacement_color)
    flood_fill(matrix, x, y + 1, target_color, replacement_color)
    flood_fill(matrix, x, y - 1, target_color, replacement_color)


def read_file(file_reference):
    with open(file_reference, 'r', encoding="UTF-8") as input_file:
        lines = input_file.read().splitlines()

    start_x, start_y = map(int, lines[1].split(','))
    replacement_color_from_file = lines[2][1]

    matrix_with_letters = []
    for line in lines[3:]:
        letters = [char for char in line if char.isalpha()]
        matrix_with_letters.append(letters)

    return matrix_with_letters, start_x, start_y, replacement_color_from_file


def write_file(matrix_with_letters, file_reference):
    with open(file_reference, 'w', encoding="UTF-8") as output_file:
        for row in matrix_with_letters:
            output_file.write('[')
            output_file.write(', '.join(row))
            output_file.write(']' + '\n')


if __name__ == "__main__":
    matrix_from_file, start_x, start_y, replacement_color_from_file = read_file("input.txt")
    flood_fill(matrix_from_file, start_x, start_y, matrix_from_file[start_x][start_y], replacement_color_from_file)
    write_file(matrix_from_file, "output.txt")
