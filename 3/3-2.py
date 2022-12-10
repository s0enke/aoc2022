f = open("input.txt", "r")
data = f.read()

priorities_sum = 0
data_arr = data.split("\n")
i = 0
while i < len(data_arr):
    priority = 0

    for first_char in data_arr[i]:
        for second_char in data_arr[i+1]:
            for third_char in data_arr[i+2]:
                if first_char == second_char and first_char == third_char:
                    print(first_char)

                    if first_char == first_char.lower():
                        priority = ord(first_char) - ord('a') + 1
                    else:
                        priority = ord(first_char) - ord('A') + 1 + 26
                    break

    i += 3
    priorities_sum += priority

print(priorities_sum)
