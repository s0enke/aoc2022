f = open("input.txt", "r")
data = f.read()

priorities_sum = 0
for line in data.split("\n"):
    first = line[0:(int(len(line)/2))]
    second = line[(int(len(line)/2)):]

    highest_prio = 0
    for first_char in first:
        for second_char in second:
            if first_char == second_char:
                if first_char == first_char.lower():
                    priority = ord(first_char) - ord('a') + 1
                else:
                    priority = ord(first_char) - ord('A') + 1 + 26
                if priority > highest_prio:
                    highest_prio = priority

    print(highest_prio)
    priorities_sum += highest_prio

print(priorities_sum)