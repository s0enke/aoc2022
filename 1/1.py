f = open("input.txt", "r")
data = f.read()

# split data by 2 newlines
values = []
for j, i in enumerate(data.split("\n\n")):
    ints = (list(map(int, i.strip().split("\n"))))
    s = sum(ints)
    values.append(s)

# get size of values

print(max(values))
