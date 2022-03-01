
def DFS(matrix, i, j):
    stack = []
    visited = []
    while True:
        probable_pos = [(i, j), (i, j - 1), (i, j + 1), (i + 1, j), (i - 1, j), (i + 1, j + 1), (i - 1, j + 1),
                        (i - 1, j - 1),
                        (i + 1, j - 1)]
        x = 0
        for k in probable_pos:
            x = x + 1
            if 0 <= k[0] < len(matrix) and 0 <= k[1] < len(matrix[0]):
                if matrix[k[0]][k[1]] == 1:
                    visited.append(k)
                    matrix[k[0]][k[1]] = 0
                    stack.append(k)

                    i = k[0]
                    j = k[1]
                    x = 0
                elif x == len(probable_pos) - 1 and len(stack) < 1:

                    return len(visited)


                elif x == len(probable_pos) - 1:
                    m = stack.pop()
                    i = m[0]
                    j = m[1]

            elif x == len(probable_pos) - 1:
                return len(visited)




matrix = []
with open('Question1 input 2.txt') as abc:
    lines = abc.readlines()

for l in lines:
    matrix.append(l.split())

k = []

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 'Y':
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0




for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            k.append(DFS(matrix, i, j))


z = sorted(k, reverse=True)
print(z[0])
