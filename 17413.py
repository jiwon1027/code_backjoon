data = list(map(str, input()))
i = 0

while i < len(data):
    if data[i] == "<":
        i += 1
        while data[i] != ">":
            i += 1
        i += 1
    elif data[i].isalnum():
        start = i
        while i < len(data) and data[i].isalnum():
            i += 1
        tmp = data[start:i]
        tmp.reverse()
        data[start:i] = tmp
    else:
        i += 1
print("".join(data))
