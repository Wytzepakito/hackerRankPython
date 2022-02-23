


def diagonalDifference(arr):
    sum_forward = 0
    sum_back = 0

    for ii in range(len(arr)):
        row = arr[ii]

        sum_forward += arr[ii][ii]
        sum_back += arr[ii][(len(arr) - 1) - ii]
    return abs(sum_forward - sum_back)

    







arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]

print(diagonalDifference(arr))