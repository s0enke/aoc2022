f = open("input.txt", "r")
data = f.read()

for i in range(len(data)):
    chunk = data[i:i+14]
    if len(chunk) == 14 and len(set(chunk)) == 14:
        print(i + 14)
        break

