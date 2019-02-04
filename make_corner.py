import sys

def corner(mat, chr='*'):
    ncols = len(mat[0])
    nrows = len(mat)

    put_at_row = [0, nrows - 1]
    for i in range(2):
        for j in range(ncols):
            mat[put_at_row[i]][j] = chr

    put_at_col = [0, ncols - 1]
    for i in range(2):
        for j in range(nrows):
            mat[j][put_at_col[i]] = chr

    return mat


def print_mat(m):
    for i in m:
        for j in i:
            sys.stdout.write("{} ".format(j))
        print()

print_mat(corner([[1,1,4,2],[1,2,5,3],[4,5,8,6],[3,4,9,5]]))

