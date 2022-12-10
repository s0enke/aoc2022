f = open("input.txt", "r")
data = f.read()

contains_counter =  0
for line in data.split("\n"):
    print("*************")
    first, second = line.split(",")
    first_start, first_end = map(int, first.split("-"))
    second_start, second_end = map(int, second.split("-"))
    print(first_start, first_end, second_start, second_end)
    if (first_start >= second_start and first_end <= second_end) or (second_start >= first_start and second_end <= first_end):
        print("CONTAINS")
        contains_counter += 1
    # print(range(first_start, first_end))
    # print(set(range(first_start, first_end)))
    # first_set = set(range(first_start, first_end))
    # second_set = set(range(second_start, second_end))
    # print(first_set, second_set)
    # if first_set.issubset(second_set) or second_set.issubset(first_set):
    #     print("CONTAINS")
    #     contains_counter += 1

print(contains_counter)