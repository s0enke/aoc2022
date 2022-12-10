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

MY_ROCK = 'X'
MY_PAPER = 'Y'
MY_SCISSORS = "Z"

MY = {
    MY_ROCK: ROCK,
    MY_PAPER: PAPER,
    MY_SCISSORS: SCISSORS,
}

SCORES = {
    MY_ROCK: 1,
    MY_PAPER: 2,
    MY_SCISSORS: 3,
}

SCORE_DRAW = 3
SCORE_WON = 6

score = 0
for line in data.split("\n"):
    if (line.strip() == ''):
        continue
    theirs, mine = line.split(" ")
    print (theirs, mine)
    if MY[mine] == THEIRS[theirs]:
        score += (SCORE_DRAW)
    elif MY[mine] == PAPER and THEIRS[theirs] == ROCK or MY[mine] == SCISSORS and THEIRS[theirs] == PAPER or MY[mine] == ROCK and THEIRS[theirs] == SCISSORS:
        score += SCORE_WON

    score += SCORES[mine]


print(score)

