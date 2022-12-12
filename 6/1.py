f = open("input.txt", "r")
data = f.read()

for i in range(len(data)):
    chunk = data[i:i+4]
    if len(chunk) == 4 and len(set(chunk)) == 4:
        print(i + 4)
        break

