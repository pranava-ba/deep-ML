def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float] | int:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    
    if not a or len(a[0]) != len(b):
        return -1

    ans = []
    for i in range(len(a)):
        ans.append(0)
        for j in range(len(b)):
            ans[i] += a[i][j] * b[j]

    return ans
