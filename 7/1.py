f = open("input.txt", "r")
data = f.read()

pwd = []
dirs = {}

for line in data.split("\n"):

    if line == "$ ls" or line.startswith("dir "):
        continue
    elif line.startswith("$ cd"):
        cd = (line[5:])
        if cd == '..':
            filesize_current_dir = dirs['/'.join(pwd)]
            print("---size of {}: {}".format('/'.join(pwd), filesize_current_dir))
            pwd.pop()
            filesize = dirs['/'.join(pwd)]
            dirs['/'.join(pwd)] += filesize_current_dir
            print("---size of {}: {} (was: {})".format('/'.join(pwd), dirs['/'.join(pwd)], filesize))
        else:
            pwd.append(cd)
            dirname = '/'.join(pwd)
            dirs[dirname] = 0
            print(" " * (len(pwd) * 2 - 2) + cd)
    else:
        filesize, filename = line.split(" ")
        dirname = '/'.join(pwd)
        print(" " * len(pwd) * 2 + filename + " " + filesize)
        dirs[dirname] += int(filesize)


total_at_most_100000 = 0
for dirname, size in dirs.items():
    if size <= 100000:
        total_at_most_100000 += size

print(total_at_most_100000)
