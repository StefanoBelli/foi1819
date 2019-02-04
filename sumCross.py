def sum_cross(mat, x, y):
    sum = 0

    if y > 0: #adjacent left
        sum += mat[x][y - 1]

    if y < len(mat[x]) - 1: #adjacent right
        sum += mat[x][y + 1]

    if x < len(mat) - 1: #adjacent below
        sum += mat[x + 1][y]

    if x > 0: #adjacent above
        sum += mat[x - 1][y]

    return sum

## test

m = [ 
      [1, 2, 3, 4],
      [4, 5, 6, 9],
      [7, 8, 9, 10],
      [11, 12, 13, 14]
    ]

print(sum_cross(m, 1, 1))
print(sum_cross(m, 0, 0))
print(sum_cross(m, 2, 2))
print(sum_cross(m, 2, 0))
print(sum_cross(m, 2, 1))
print(sum_cross(m, 0, 1))
print(sum_cross(m, 3, 1))
