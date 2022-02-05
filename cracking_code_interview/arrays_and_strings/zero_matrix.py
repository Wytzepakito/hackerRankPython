

def set_zero(mat):

    ver_inds =[]
    hor_inds =[]

    for y in range(len(mat)):
        for x in range(len(mat)):

            if mat[y][x] == 0:
                ver_inds.append(x)
                hor_inds.append(y)

    for x, y in zip(ver_inds, hor_inds):

        for i in range(len(mat)):
            if x is not None:
                mat[i][x] = 0
            if y is not None:
                mat[y][i] = 0

    for row in mat:
        print(row)










mat = [[1, 2, 3, 4, 5, 6],
        [0, 2, 3, 4, 5, 6],
        [4, 5, 6, 7, 8, 9],
        [0, 2, 2, 1 ,1, 1],
        [9, 9, 9, 9, 2, 1],
        [8, 7, 6, 5, 4, 0]]


set_zero(mat)
