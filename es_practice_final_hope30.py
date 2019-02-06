import sys

###

def count(L, s1, s2):
    counter = 0

    for idx in range(len(L) - 1):
        if L[idx] == s1 and L[idx + 1] == s2:
            counter += 1

    return counter

print(count(['a','b', 'ab', 'b'], 'ab','b'))

####

def plusOne(M):
    for idx in range(len(M[0])):
        if M[0][idx] == 0:
            for row_idx in range(len(M)):
                M[row_idx][idx] += 1

    return M

mat = [
        [0,1,0,3],
        [1,2,0,1],
        [1,1,3,2]
        ]

def printMatrix(M):
    for i in M:
        for j in i:
            sys.stdout.write("{} ".format(j))

        print()

printMatrix(plusOne(mat))
