# Lab 1 Task 1
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



# Lab 1 Task 2


def BFS(matrix, i, j):

    queue = []
    time = 0
    visited = []

    while True:
        found = False

        probable_pos = [(i, j - 1), (i, j + 1), (i + 1, j), (i - 1, j)]
        if 0 <= probable_pos[0][0] < len(matrix) and 0 <= probable_pos[0][1] < len(matrix[0]) and \
                matrix[probable_pos[0][0]][probable_pos[0][1]] == 0 and probable_pos[0] not in visited:
            queue.append(probable_pos[0])
            matrix[probable_pos[0][0]][probable_pos[0][1]] = 1

            visited.append(probable_pos[0])
            found = True

        if 0 <= probable_pos[1][0] < len(matrix) and 0 <= probable_pos[1][1] < len(matrix[0]) and \
                matrix[probable_pos[1][0]][probable_pos[1][1]] == 0 and probable_pos[1] not in visited:
            queue.append(probable_pos[1])
            matrix[probable_pos[1][0]][probable_pos[1][1]] = 1

            visited.append(probable_pos[1])
            found = True

        if 0 <= probable_pos[2][0] < len(matrix) and 0 <= probable_pos[2][1] < len(matrix[0]) and \
                matrix[probable_pos[2][0]][probable_pos[2][1]] == 0 and probable_pos[2] not in visited:
            queue.append(probable_pos[2])
            matrix[probable_pos[2][0]][probable_pos[2][1]] = 1

            visited.append(probable_pos[2])
            found = True

        if 0 <= probable_pos[3][0] < len(matrix) and 0 <= probable_pos[3][1] < len(matrix[0]) and \
                matrix[probable_pos[3][0]][probable_pos[3][1]] == 0 and probable_pos[3] not in visited:
            queue.append(probable_pos[3])
            matrix[probable_pos[3][0]][probable_pos[3][1]] = 1

            visited.append(probable_pos[3])
            found = True


        if len(queue) < 1:
            return time

        if found:
            time = time + 1
        i, j = queue.pop(0)






matrix = []
with open('Question2 input2.txt') as abc:
    lines = abc.readlines()

for l in lines:
    matrix.append(l.split())

k = []

row = int(matrix.pop(0).pop(0))
col = int(matrix.pop(0).pop(0))

for i in range(row):
    for j in range(col):
        if matrix[i][j] == 'A':
            matrix[i][j] = 1
        elif matrix[i][j] == 'H':
            matrix[i][j] = 0
        else:
            matrix[i][j] = -1


alien_pos = list()
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            alien_pos.append((i, j))

for i in alien_pos:
    x = BFS(matrix, i[0], i[1])
    k.append(x)


z = sorted(k, reverse=True)


print("Time: {} minutes".format(z[0]))
x = 0
for i in range(row):
    for j in range(col):
        if matrix[i][j] == 0:
            x = x + 1

if x == 0:
    print("No one survived")
else:
    print("{} survived".format(x))


