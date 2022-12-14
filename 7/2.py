f = open("input.txt", "r")
data = f.read()

from anytree import Node, RenderTree, PreOrderIter

root = wd = Node("", total_size=0)

for line in data.split("\n"):

    if line == "$ ls" or line.startswith("dir "):
        continue
    elif line.startswith("$ cd"):
        cd = (line[5:])
        if cd == '..':
            wd = wd.parent
        else:
            if cd == '/':
                wd = root
                continue
            wd = Node(cd, parent=wd, total_size=0)
    else:
        filesize, filename = line.split(" ")
        for parent_node in wd.iter_path_reverse():
            parent_node.total_size += int(filesize)

total_used_size = root.total_size
total_disk_size = 70000000
need_unused_space = 30000000
need_to_free = -(total_disk_size - total_used_size - need_unused_space)
directories_bigger_than_need_to_free = [node.total_size for node in PreOrderIter(root, filter_=lambda n: n.total_size >= need_to_free)]
directories_bigger_than_need_to_free.sort()
print(directories_bigger_than_need_to_free[0])
