N=4
def reverseDiagonal(array):
    i = 0
    j = N
    while (i < j):
        array[i][i], array[j - 1][j - 1] = array[j - 1][j - 1], array[i][i]
        array[i][j - 1], array[j - 1][i] = array[j - 1][i], array[i][j - 1]

        i += 1
        j -= 1

    for i in range(N):
        for j in range(N):
            print(array[i][j], end="  ")
        print()

if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    reverseDiagonal(matrix)