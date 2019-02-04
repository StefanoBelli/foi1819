
def croce(A, i, j):

    for ru in range(0, i):
        if A[i][j] < A[ru][j]:
            return False

    for rd in range(i+1, len(A)):
        if A[i][j] < A[rd][j]:         # comparazione da riga a riga
            return False

    for cr in range(j+1, len(A[i])): 
        if A[i][j] < A[i][cr]:     # comparazione colonna a colonna
            return False
    
    for cl in range(0, j): 
        if A[i][j] < A[i][cl]:
            return False


    return True

m = [ 
        [2,1,3,10], 
        [3,4,2,4],
        [4,4,2,5],
        [6,0,2,8]
    ]

print(croce(m, 0, 3))
