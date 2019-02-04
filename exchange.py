def exchange(A, x, y):
    rowslen = len(A)
    for xi in range(rowslen):
        if rowslen != len(A[xi]):
            return False

    col_x = list()
    for yidx in range(rowslen):
        col_x.append(A[yidx][x])

    row_y = A[y]

    A[y] = col_x

    for yidx in range(rowslen):
        A[yidx][x] = row_y[yidx]

    return True

A = [ [1,2,6,7], 
      [3,4,5,8],
      [9,10,11,12],
      [1,2,3,3] ]

exchange(A, x=2, y=2)

print(A)
