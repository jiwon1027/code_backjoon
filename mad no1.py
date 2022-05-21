entry_log = [2, 1, 3, 4,-3,-4,-1,-2, 5,-5, 1, 6,-1,-6]
infect = 1

data = []
res = set()
def check(temp):
    if infect in temp:
        idx = temp.index(infect)
        if idx-1 >= 0:
            res.add(temp[idx-1])
        if idx+1 < len(temp):
            res.add(temp[idx+1])


for i in range(len(entry_log)):
    if entry_log[i] > 0:
        data.append(entry_log[i])
    else:
        data.remove(-entry_log[i])
    print(data)

    check(data)

print(res)


