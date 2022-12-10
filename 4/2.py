f = open("input.txt", "r")
data = f.read()

has_intersection_counter =  0
for line in data.split("\n"):
    print("*************")
    first, second = line.split(",")
    first_start, first_end = map(int, first.split("-"))
    second_start, second_end = map(int, second.split("-"))
    print(first_start, first_end, second_start, second_end)
    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))
    print(len(first_set.intersection(second_set)))
    if len(first_set.intersection(second_set)) > 0:
        has_intersection_counter += 1

print(has_intersection_counter)