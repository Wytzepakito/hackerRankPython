def get_path(mat):
    if mat == None or len(mat) == 0:
        return
    
    c = 0 
    r = 0
    paths = []
    if get_my_path(mat, len(mat) - 1, len(mat) -1, paths):
        return paths
    else:
        return None


def get_my_path(mat, row, col, path):
    if (row < 0 or col < 0 or mat[row][col] == 1):
        return False

    isAtOrigin = (row == 0) and (col == 0)

    if (isAtOrigin or get_my_path(mat, row -1, col, path) or get_my_path(mat, row, col -1, path)):
        point = (row,col)
        path.append(point)
        return True

    return False






mat = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[ 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
[ 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
[ 0, 0, 0, 0, 1, 1, 1, 0, 1, 0],
[ 0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
[ 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
[ 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[ 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[ 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
 ]


print(get_path(mat))