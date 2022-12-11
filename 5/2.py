f = open("input.txt", "r")
data = f.read()

stacks_raw, instructions = data.split("\n\n")

print(stacks_raw)

stack_raw_arr = stacks_raw.split("\n")
stack_raw_arr.pop()
stack_raw_arr.reverse()

print(stack_raw_arr)

stacks = {}
for stack_id in range(1, 10):
    stacks[stack_id] = []
    for i in range(0, len(stack_raw_arr)):
        offset = (stack_id - 1) * 4 + 1
        stack_value = stack_raw_arr[i][offset]
        if stack_value != ' ':
            stacks[stack_id].append(stack_value)

for instruction_raw in instructions.split("\n"):
    instructions_arr = instruction_raw.split(" ")
    how_many, from_stack, to_stack = map(int, [instructions_arr[1], instructions_arr[3], instructions_arr[5]])
    tmp = []
    for i in range(how_many):
        tmp.append(stacks[from_stack].pop())
    tmp.reverse()

    stacks[to_stack].extend(tmp)

print(stacks)

for stack in stacks.values():
    print(stack[len(stack) - 1], end='')

print()
