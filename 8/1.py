f = open("input.txt", "r")
data = f.read()

import numpy
matrix = []
for line in data.split("\n"):
    tmp = []
    for x in line:
        tmp.append(x)
    matrix.append(tmp)

matrix = numpy.array(matrix)

counter = 0
for y, xs in enumerate(matrix):
    if y == 0 or y == (len(matrix) - 1):
        counter += len(matrix)
        continue

    for x, height in enumerate(xs):
        if x == 0 or x == (len(xs) - 1):
            counter += 1
            continue

        if height > max(matrix[y, 0:x]) or height > max(matrix[y, x+1:]) or height > max(matrix[0:y, x]) or height > max(matrix[y+1:, x]):
            counter += 1
            print("found {} at {}, {}".format(height, y, x))

print(counter)