
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
with open('Question2 input1.txt') as abc:
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


