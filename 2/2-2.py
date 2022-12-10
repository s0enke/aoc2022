f = open("input.txt", "r")
data = f.read()

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

THEIR_ROCK = 'A'
THEIR_PAPER = "B"
THEIR_SCISSORS = 'C'

THEIRS = {
    THEIR_ROCK: ROCK,
    THEIR_PAPER: PAPER,
    THEIR_SCISSORS: SCISSORS,
}

MY_LOSE = 'X'
MY_DRAW = 'Y'
MY_WIN = "Z"


SCORES = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}

SCORE_DRAW = 3
SCORE_WON = 6

score = 0
for line in data.split("\n"):
    if (line.strip() == ''):
        continue
    theirs, mine = line.split(" ")
    print(theirs, mine)

    if mine == MY_LOSE:
        if theirs == THEIR_PAPER:
            score += SCORES[ROCK]
        elif theirs == THEIR_ROCK:
            score += SCORES[SCISSORS]
        elif theirs == THEIR_SCISSORS:
            score += SCORES[PAPER]
        else:
            raise RuntimeError
    elif mine == MY_DRAW:
        score += SCORE_DRAW
        if theirs == THEIR_PAPER:
            score += SCORES[PAPER]
        elif theirs == THEIR_ROCK:
            score += SCORES[ROCK]
        elif theirs == THEIR_SCISSORS:
            score += SCORES[SCISSORS]
        else:
            raise RuntimeError
    elif mine == MY_WIN:
        score += SCORE_WON
        if theirs == THEIR_PAPER:
            score += SCORES[SCISSORS]
        elif theirs == THEIR_ROCK:
            score += SCORES[PAPER]
        elif theirs == THEIR_SCISSORS:
            score += SCORES[ROCK]
        else:
            raise RuntimeError
    else:
        raise RuntimeError



print(score)

