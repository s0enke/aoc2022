
def score_of_highest_field(filename):
    f = open(filename, "r")
    data = f.read()

    import numpy
    matrix = []
    for line in data.split("\n"):
        tmp = []
        for x in line:
            tmp.append(int(x))
        matrix.append(tmp)

    matrix = numpy.array(matrix)

    highest_score = 0
    for y, xs in enumerate(matrix):
        for x, height in enumerate(xs):
            score = 1
            for direction_slice in [matrix[y, x+1:], numpy.flip(matrix[y, 0:x]), matrix[y+1:, x], numpy.flip(matrix[0:y, x])]:
                try:
                    tmp_score = numpy.argwhere(direction_slice >= height)[0][0] + 1
                except IndexError:
                    tmp_score = len(direction_slice)
                score *= tmp_score

            if score > highest_score:
                highest_score = score

    return highest_score
