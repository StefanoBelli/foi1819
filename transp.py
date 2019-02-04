import sys
def transp(M):
    new_mat = []

    for i in range(len(M[0])):
        new_mat.append([])
        for j in range(len(M)):
            new_mat[i].append([])

    for new_row_idx in range(len(M)):
        for new_col_idx in range(len(M[0])):
            new_mat[new_col_idx][new_row_idx] = M[new_row_idx][new_col_idx]

    return new_mat

def print_matrix(m):
    for r in m:
        for c in r:
            sys.stdout.write("{} ".format(c))
        print("")

x = [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ]
print_matrix(x)
print("\nTrasposta: ")
print_matrix(transp(x))
