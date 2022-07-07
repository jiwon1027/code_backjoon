string = input()
res = 0

for start in range(len(string)):
    for end in range(start + 1, len(string)):

        if string[start] == string[end]:
            data = []
            for idx in range(start, end + 1):
                data.append(string[idx])

            for temp in data:
                if data.count(temp) == 1:
                    res += 1
            break

print(res // 2)
