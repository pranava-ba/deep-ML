def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == 'row':
        result = []
        for row in matrix:
            result.append(sum(row) / len(row))
        return result

    elif mode == 'column':
        result = []
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        for col in range(num_cols):
            s = 0
            for row in range(num_rows):
                s += matrix[row][col]
            result.append(s / num_rows)

        return result
